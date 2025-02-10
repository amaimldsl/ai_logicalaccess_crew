from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.access_review import AccessReview
from tools.transaction_approval_review import TransactionApprovalReview
from tools.change_management_verification import ChangeManagementVerification
from tools.transaction_policy_review import TransactionPolicyReview
import os
import time
from pathlib import Path
from typing import List, Dict
from litellm.exceptions import RateLimitError


from crewai import Agent, Crew, Process, Task, LLM
import time
from typing import Optional
from litellm.exceptions import RateLimitError, APIError
import json
import logging

class DeepseekAPIWrapper:
    def __init__(self, max_retries=3, base_delay=1, max_delay=32):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        
    def handle_call(self, func, *args, **kwargs):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                return func(*args, **kwargs)
            except (APIError, RateLimitError) as e:
                retry_count += 1
                if retry_count == self.max_retries:
                    raise
                
                delay = min(self.base_delay * (2 ** retry_count), self.max_delay)
                logging.warning(f"API call failed (attempt {retry_count}): {str(e)}")
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            except json.JSONDecodeError as e:
                retry_count += 1
                if retry_count == self.max_retries:
                    raise APIError(f"Failed to decode JSON response after {self.max_retries} attempts")
                
                delay = min(self.base_delay * (2 ** retry_count), self.max_delay)
                logging.warning(f"JSON decode error (attempt {retry_count}): {str(e)}")
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)

class EnhancedLLM(LLM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_wrapper = DeepseekAPIWrapper()
        
    def generate(self, *args, **kwargs):
        return self.api_wrapper.handle_call(super().generate, *args, **kwargs)
    
    def chat(self, *args, **kwargs):
        return self.api_wrapper.handle_call(super().chat, *args, **kwargs)

@CrewBase
class Larc():
    def __init__(self, deepseek_api_key, deepseek_api_base, deepseek_model):
        os.environ['LITELLM_LOG'] = 'DEBUG'
        os.environ['DEEPSEEK_API_KEY'] = deepseek_api_key
        os.environ['DEEPSEEK_BASE_URL'] = deepseek_api_base

        self.agent_llm = EnhancedLLM(
            model=deepseek_model,
            api_key=deepseek_api_key,
            base_url=deepseek_api_base
        )


        LLAMA31_LLM = LLM(model="ollama/llama3.1")
        MISTRAL_LLM = LLM(model="ollama/mistral")
        LLAMA32_LLM = LLM(model="ollama/llama3.2")
        LLAMA33_LLM = LLM(model="ollama/llama3.3")
        MIXTRAL_LLM = LLM(model="ollama/mixtral")
        
        DEEPSEEK_LC_DF_LLM =  LLM(model="ollama/deepseek-r1")
        DEEPSEEK_LCL_14B_LLM =  LLM(model="ollama/deepseek-r1:14b")
        DEEPSEEK_LCL_32B_LLM =  LLM(model="ollama/deepseek-r1:32b")

                

        def create_groc_ds_llm():
            """Initialize the Groq DeepSeek LLM with rate limit handling."""
            
            return LLM(
                model="groq/deepseek-r1-distill-llama-70b",
                max_retries=5,
                timeout=30,
                service_tier="on_demand",
                #max_tokens=2048,  # Reduced from 1024 to 768
                
            )
            
            
                
        # Initialize LLM with retry handling
        GROC_DS_LLM = create_groc_ds_llm()

        #self.agent_llm = DEEPSEEK_LLM

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    access_review = AccessReview()
    limit_review = TransactionApprovalReview()
    trail_review = ChangeManagementVerification()
    trans_policy_review = TransactionPolicyReview()

    @agent
    def logical_access_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['logical_access_reviewer'],
            verbose=True,
            llm=self.agent_llm,
            #max_rpm=30  
        )

    @agent
    def limit_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['limit_reviewer'],
            verbose=True,
            llm=self.agent_llm,
            #max_rpm=30  
        )
    
    @agent
    def transaction_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['transaction_reviewer'],
            verbose=True,
            llm=self.agent_llm,
            #max_rpm=30  
        )
    
    @agent
    def audit_trail_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['audit_trail_reviewer'],
            verbose=True,
            llm=self.agent_llm,
            #max_rpm=30  
        )

    @agent
    def audit_report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['audit_report_writer'],
            verbose=True,
            llm=self.agent_llm,
            #max_rpm=30  
        )
    
    @task
    def review_logical_access(self) -> Task:
        return Task(
            config=self.tasks_config['review_logical_access'],
            tools=[self.access_review.access_review_tool],
            llm=self.agent_llm,
            output_file="findings/LogicalAccessObservation.md",
        )

    @task
    def review_transaction_limits(self) -> Task:
        return Task(
            config=self.tasks_config['review_transaction_limits'],
            tools=[self.limit_review.limit_review_tool],
            llm=self.agent_llm,
            output_file="findings/TransactionsLimitsObservation.md",
        )

    @task
    def review_audit_trail(self) -> Task:
        return Task(
            config=self.tasks_config['review_audit_trail'],
            tools=[self.trail_review.change_management_verification_tool],
            llm=self.agent_llm,
            output_file="findings/AuditTrailObservation.md",
        )
    
    @task
    def review_transaction_policy(self) -> Task:
        return Task(
            config=self.tasks_config['review_transaction_policy'],
            tools=[self.trans_policy_review.transaction_policy_review_tool],
            llm=self.agent_llm,
            output_file="findings/TransactionsComplianceObservation.md",
        )
    
    @task
    def compile_audit_report(self) -> Task:
        return Task(
        config=self.tasks_config['compile_audit_report'],
        llm=self.agent_llm,
        tools=[
            self.access_review.access_review_tool,
            self.limit_review.limit_review_tool,
            self.trail_review.change_management_verification_tool,
            self.trans_policy_review.transaction_policy_review_tool
        ],
        output_file="DraftAuditReport.md",
        context=[
            self.review_logical_access(),
            self.review_transaction_limits(),
            self.review_audit_trail(),
            self.review_transaction_policy()
        ],
        description="Compile findings from markdown files in chronological risk order (Critical->Low), including Executive Summary and Detailed Findings with root cause analysis."
    )
    
    
    
    @crew
    def crew(self) -> Crew:
        """Creates the Larc crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            #max_rpm=30  # This will override individual agent settings
        )

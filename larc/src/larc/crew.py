from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, DirectoryReadTool
from tools.access_review import AccessReview
import litellm
from tools.transaction_approval_review import TransactionApprovalReview
from tools.change_management_verification import ChangeManagementVerification
from tools.transaction_policy_review import TransactionPolicyReview
import os
import time
from pathlib import Path
from typing import List, Dict
from litellm.exceptions import RateLimitError, APIError
import json
import logging


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Print to console
        logging.FileHandler('api_calls.log')  # Also save to file
    ]
)


class DeepseekAPIWrapper:
    def __init__(self, max_retries=999, base_delay=1, max_delay=32):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.logger = logging.getLogger(__name__)
        
    def handle_call(self, func, *args, **kwargs):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                self.logger.debug(f"Attempt {retry_count + 1} of API call")
                return func(*args, **kwargs)
            except (APIError, litellm.exceptions.APIError) as e:  # Add litellm.exceptions.APIError
                retry_count += 1
                
                # Log the full error for debugging
                self.logger.error(f"Full error details: {str(e)}")
                
                if retry_count == self.max_retries:
                    self.logger.error(f"Max retries ({self.max_retries}) reached. Giving up.")
                    raise
                
                delay = min(self.base_delay * (2 ** retry_count), self.max_delay)
                self.logger.warning(f"API error (attempt {retry_count}): {str(e)}")
                self.logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                
            except Exception as e:
                self.logger.error(f"Unexpected error type {type(e)}: {str(e)}")
                raise






class EnhancedLLM(LLM):
    def __init__(self, *args, max_retries=999, base_delay=1, max_delay=32, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.logger = logging.getLogger(__name__)

    def chat(self, *args, **kwargs):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                return super().chat(*args, **kwargs)
            except APIError as e:
                retry_count += 1
                #self.logger.error(f"API error on attempt {retry_count}: {str(e)}")
                
                if retry_count >= self.max_retries:
                    self.logger.error("Max retries reached, raising error")
                    raise
                
                delay = min(self.base_delay * (2 ** retry_count), self.max_delay)
                self.logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)

    def call(self, *args, **kwargs):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                return super().call(*args, **kwargs)
            except APIError as e:
                retry_count += 1
                self.logger.error(f"API error on attempt {retry_count}: {str(e)}")
                
                if retry_count >= self.max_retries:
                    self.logger.error("Max retries reached, raising error")
                    raise
                
                delay = min(self.base_delay * (2 ** retry_count), self.max_delay)
                self.logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)



@CrewBase
class Larc():
    def __init__(self, deepseek_api_key, deepseek_api_base, deepseek_model):
        
        
        # Configure logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('larc.log')
            ]
        )

      
        
        #########
        
        

        LLAMA31_LLM = LLM(model="ollama/llama3.1")
        MISTRAL_LLM = LLM(model="ollama/mistral")
        LLAMA32_LLM = LLM(model="ollama/llama3.2")
        LLAMA33_LLM = LLM(model="ollama/llama3.3")
        MIXTRAL_LLM = LLM(model="ollama/mixtral")
        
        DEEPSEEK_LC_DF_LLM =  LLM(model="ollama/deepseek-r1")
        DEEPSEEK_LCL_14B_LLM =  LLM(model="ollama/deepseek-r1:14b")
        DEEPSEEK_LCL_32B_LLM =  LLM(model="ollama/deepseek-r1:32b")


        DEEPSEEK_LLM=   EnhancedLLM(
            model=deepseek_model,
            api_key=deepseek_api_key,
            base_url=deepseek_api_base,
            max_retries=999,  # You can adjust these values
            base_delay=2,
            max_delay=61
        )

        self.agent_llm = MISTRAL_LLM

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


    # Define tools
    file_tool = FileReadTool()
    directory_tool = DirectoryReadTool(directory='./findings')


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
        output_file="DraftAuditReport.md",
        tools=[self.directory_tool,self.file_tool],
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

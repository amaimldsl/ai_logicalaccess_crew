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

@CrewBase
class Larc():
    """Larc crew"""

    def __init__(self, deepseek_api_key, deepseek_api_base, deepseek_model):
        """
        Initialize the Larc crew with the DeepSeek configuration.
        """
        os.environ['LITELLM_LOG'] = 'DEBUG'  # Replace deprecated set_verbose
        os.environ['DEEPSEEK_API_KEY'] = deepseek_api_key
        os.environ['DEEPSEEK_BASE_URL'] = deepseek_api_base

        DEEPSEEK_LLM = LLM(
            model="deepseek/" + deepseek_model,
            api_key=os.getenv('DEEPSEEK_API_KEY'),
            base_url=os.getenv('DEEPSEEK_BASE_URL')
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
                max_tokens=2048,  # Reduced from 1024 to 768
                
            )
            
            
                
        # Initialize LLM with retry handling
        GROC_DS_LLM = create_groc_ds_llm()

        self.agent_llm = GROC_DS_LLM

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
        )

    @agent
    def limit_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['limit_reviewer'],
            verbose=True,
            llm=self.agent_llm,
        )
    
    @agent
    def transaction_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['transaction_reviewer'],
            verbose=True,
            llm=self.agent_llm,
        )
    
    @agent
    def audit_trail_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['audit_trail_reviewer'],
            verbose=True,
            llm=self.agent_llm,
        )

    @agent
    def audit_report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['audit_report_writer'],
            verbose=True,
            llm=self.agent_llm,
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
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Larc crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            max_rpm=30  # This will override individual agent settings
        )

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

        self.agent_llm = DEEPSEEK_LLM

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
            function=lambda result: {
                'source': 'LogicalAccessObservation.md',
                'content': result
            }
        )

    @task
    def review_transaction_limits(self) -> Task:
       
        return Task(
            config=self.tasks_config['review_transaction_limits'],
            tools=[self.limit_review.limit_review_tool],
            llm=self.agent_llm,
            output_file="findings/TransactionsLimitsObservation.md",
            function=lambda result: {
                'source': 'TransactionsLimitsObservation.md',
                'content': result
            }
        )

    @task
    def review_audit_trail(self) -> Task:
     
        return Task(
            config=self.tasks_config['review_audit_trail'],
            tools=[self.trail_review.change_management_verification_tool],
            llm=self.agent_llm,
            output_file="findings/AuditTrailObservation.md",
            function=lambda result: {
                'source': 'AuditTrailObservation.md',
                'content': result
            }
        )
    
    @task
    def review_transaction_policy(self) -> Task:
      
        
        return Task(
            config=self.tasks_config['review_transaction_policy'],
            tools=[self.trans_policy_review.transaction_policy_review_tool],
            llm=self.agent_llm,
            output_file="findings/TransactionsComplianceObservation.md",
            function=lambda result: {
                'source': 'TransactionsComplianceObservation.md',
                'content': result
            }
        )
    
    @task
    def compile_audit_report(self) -> Task:
        def read_findings() -> List[Dict[str, str]]:
            """
            Read findings from the findings directory relative to the current script location.
            Returns a list of dictionaries containing source and content.
            """
            findings = []
            current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
            findings_dir = current_dir / "findings"
            
            try:
                findings_dir.mkdir(exist_ok=True)
                
                if not findings_dir.is_dir():
                    print(f"Findings directory not found at {findings_dir}")
                    return []
                    
                for file_path in findings_dir.glob("*.md"):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            findings.append({
                                'source': file_path.name,
                                'content': f.read().strip()
                            })
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
                        continue
                        
            except Exception as e:
                print(f"Error accessing findings directory: {e}")
                return []
                
            return findings

        # Read findings from files (fallback if context is not available)
        findings = read_findings()
        context_list = [f"Finding from {f['source']}: {f['content']}" for f in findings]

     

        return Task(
            config=self.tasks_config['compile_audit_report'],
            llm=self.agent_llm,
            context=context_list,  # Pass findings as context
            output_file="DraftAuditReport.md"
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Larc crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
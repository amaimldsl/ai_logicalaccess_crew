from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from tools.access_review import AccessReview
from tools.transaction_approval_review import TransactionApprovalReview
from tools.change_management_verification import ChangeManagementVerification
from tools.transaction_policy_review import TransactionPolicyReview
import os
import litellm
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
        #litellm.set_verbose=True
        #if not deepseek_api_key or not deepseek_api_base or not deepseek_model:
        #    raise ValueError("One or more DeepSeek parameters are missing.")
        #print(f"API Key: {deepseek_api_key}, Base URL: {deepseek_api_base}, Model: {deepseek_model}")
        #Continue with your LLM initialization

        #DEEPSEEK_LLM = LLM(
        #        api_key=deepseek_api_key,
        #        base_url=deepseek_api_base,  # Set the DeepSeek API base URL
        #        model=deepseek_model
        #)

        #DEEPSEEK_LLM = LLM(
        #    model=f"deepseek/{deepseek_model}",
        #    model=deepseek_model,
        #    base_url=deepseek_api_base,
        #    api_key=deepseek_api_key,
        #    temperature=0.3,
        #    # Force response format to JSON (critical fix)
        #    response_format={"type": "json_object"},
        #    # Add custom headers if required by DeepSeek
        #    headers={
        #        "Content-Type": "application/json",
        #        "Accept": "application/json"
        #    }
        #)
        

        #DEEPSEEK_LLM = LLM(
        #api_key=deepseek_api_key,
        #base_url=deepseek_api_base,  # Set the DeepSeek API base URL
        #model=deepseek_model
    #)
        # Set up your API key (preferably using environment variables)
        
        os.environ['DEEPSEEK_API_KEY'] = deepseek_api_key
        os.environ['DEEPSEEK_BASE_URL'] = deepseek_api_base

        DEEPSEEK_LLM = LLM(
            model="deepseek/" + deepseek_model,
            api_key=os.getenv('DEEPSEEK_API_KEY'),
            base_url=os.getenv('DEEPSEEK_BASE_URL')
        )

        # Create the crewai.LLM object
        #DEEPSEEK_LLM = LLM(model="deepseek/deepseek-chat")
        DEEPSEEK_LLM = LLM(model="deepseek/" + deepseek_model)


        LLAMA31_LLM = LLM(model="ollama/llama3.1")
        MISTRAL_LLM = LLM(model="ollama/mistral")
        LLAMA32_LLM = LLM(model="ollama/llama3.2")
        LLAMA33_LLM = LLM(model="ollama/llama3.3")
        MIXTRAL_LLM = LLM(model="ollama/mixtral")
        
        DEEPSEEK_LC_DF_LLM =  LLM(model="ollama/deepseek-r1")
        DEEPSEEK_LCL_14B_LLM =  LLM(model="ollama/deepseek-r1:14b")
        DEEPSEEK_LCL_32B_LLM =  LLM(model="ollama/deepseek-r1:32b")
        
        self.agent_llm = LLAMA31_LLM

    #litellm.set_verbose = True
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
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
            llm = self.agent_llm,
            #async_execution=True,
            output_file="findings/LogicalAccessObservation.md",
        )

    
    @task
    def review_transaction_limits(self) -> Task:
        return Task(
            config=self.tasks_config['review_transaction_limits'],
            tools=[self.limit_review.limit_review_tool],
            llm = self.agent_llm,
            #async_execution=True,
            output_file="findings/TransactionsLimitsObservation.md",
        )

    
    @task
    def review_audit_trail(self) -> Task:
        return Task(
            config=self.tasks_config['review_audit_trail'],
            tools=[self.trail_review.change_management_verification_tool],
            llm = self.agent_llm,
            #async_execution=True,
            output_file="findings/AuditTrailObservation.md",
            
        )
    
    
    @task
    def review_transaction_policy(self) -> Task:
        return Task(
            config=self.tasks_config['review_transaction_policy'],
            tools=[self.trans_policy_review.transaction_policy_review_tool],
            llm = self.agent_llm,
            #async_execution=True,
            output_file="findings/TransactionsComplianceObservation.md",
            
        )
    

    @task
    def compile_audit_report(self) -> Task:
        def read_findings() -> List[Dict[str, str]]:
            """
            Read findings from the findings directory relative to the current script location
            Returns a list of dictionaries containing source and content
            """
            findings = []
            
            # Get the directory of the currently executing script
            current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
            findings_dir = current_dir / "findings"
            
            try:
                findings_dir.mkdir(exist_ok=True)
                
                # Check if directory exists and is accessible
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
                
            if not findings:
                print(f"No .md files found in {findings_dir}")
                
            return findings

        # Get findings context
        findings = read_findings()
        context_list = [f"Finding from {f['source']}: {f['content']}" for f in findings]
        
        return Task(
            config=self.tasks_config['compile_audit_report'],
            llm=self.agent_llm,
            context=context_list,  # Added context to the Task
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
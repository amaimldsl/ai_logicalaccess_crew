from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from tools.access_review import AccessReview
from tools.transaction_approval_review import TransactionApprovalReview

@CrewBase
class Larc():
    """Larc crew"""

    def __init__(self, deepseek_api_key, deepseek_api_base, deepseek_model):
        """
        Initialize the Larc crew with the DeepSeek configuration.
        """

        if not deepseek_api_key or not deepseek_api_base or not deepseek_model:
            raise ValueError("One or more DeepSeek parameters are missing.")
        print(f"API Key: {deepseek_api_key}, Base URL: {deepseek_api_base}, Model: {deepseek_model}")
        #Continue with your LLM initialization

        DEEPSEEK_LLM = LLM(
                api_key=deepseek_api_key,
                base_url=deepseek_api_base,  # Set the DeepSeek API base URL
                model=deepseek_model
        )
        
        LLAMA31_LLM = LLM(model="ollama/llama3.1")
        MISTRAL_LLM = LLM(model="ollama/mistral")
        LLAMA32_LLM = LLM(model="ollama/llama3.2")
        DEEPSEEK_LCL_LLM =  LLM(model="ollama/deepseek-r1")
        
        self.agent_llm = DEEPSEEK_LLM

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    access_review = AccessReview()
    limit_review = TransactionApprovalReview()

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
            
        )

    
    @task
    def review_transaction_limits(self) -> Task:
        return Task(
            config=self.tasks_config['review_transaction_limits'],
            tools=[self.limit_review.access_review_tool],
            
        )

    
    
    
    
    
    
    
    @task
    def compile_audit_report(self) -> Task:
        return Task(
            config=self.tasks_config['compile_audit_report'],
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
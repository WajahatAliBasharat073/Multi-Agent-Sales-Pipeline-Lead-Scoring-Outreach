from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from src.agents import get_sales_rep_agent, get_lead_sales_rep_agent, get_lead_scorer_agent
from src.tasks import get_lead_profiling_task, get_scoring_task, get_outreach_task
from src.utils import get_model_name

def build_sales_pipeline_crew():
    """
    Assembles the Sales Pipeline Crew using a Hierarchical process.
    """
    # 1. Initialize Agents
    sales_rep = get_sales_rep_agent()
    lead_sales_rep = get_lead_sales_rep_agent()
    lead_scorer = get_lead_scorer_agent()

    # 2. Define Tasks and their dependencies
    profiling_task = get_lead_profiling_task(sales_rep)
    scoring_task = get_scoring_task(lead_scorer, [profiling_task])
    outreach_task = get_outreach_task(lead_sales_rep, [profiling_task, scoring_task])

    # 3. Configure Manager LLM
    # Hierarchical process requires a manager to coordinate
    manager_llm = ChatOpenAI(model=get_model_name(), temperature=0)

    # 4. Assemble the Crew
    crew = Crew(
        agents=[sales_rep, lead_sales_rep, lead_scorer],
        tasks=[profiling_task, scoring_task, outreach_task],
        process=Process.hierarchical,
        manager_llm=manager_llm,
        memory=True,
        verbose=True
    )
    
    return crew

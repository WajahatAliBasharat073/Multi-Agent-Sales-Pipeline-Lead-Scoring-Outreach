from crewai import Task
from src.tools import get_directory_read_tool, get_file_read_tool, get_search_tool, get_sentiment_tool

def get_lead_profiling_task(agent):
    return Task(
        description=(
            "Conduct an in-depth analysis of {lead_name}, "
            "a company in the {industry} sector. "
            "Utilize all available data sources to compile a detailed profile, "
            "focusing on key decision-makers, recent business developments, and potential needs."
        ),
        expected_output=(
            "A comprehensive report on {lead_name}, including company background, "
            "key personnel, recent milestones, and identified needs."
        ),
        tools=[get_directory_read_tool(), get_file_read_tool(), get_search_tool()],
        agent=agent,
    )

def get_scoring_task(agent, context_tasks):
    return Task(
        description=(
            "Analyze the profile of {lead_name} and assign a score based on {industry} trends. "
            "Consider factors like company size, market position, and potential for AI adoption."
        ),
        expected_output=(
            "A lead score (1-10) with a 2-sentence justification. "
            "If score < 7, suggest a passive approach."
        ),
        agent=agent,
        context=context_tasks
    )

def get_outreach_task(agent, context_tasks):
    return Task(
        description=(
            "Using the insights from the profiling and scoring reports on {lead_name}, "
            "craft a personalized outreach campaign aimed at {key_decision_maker}, "
            "the {position} of {lead_name}. "
            "Address their recent {milestone} and maintain a professional tone."
        ),
        expected_output=(
            "A JSON object containing:\n"
            "{\n"
            "  \"lead_score\": int,\n"
            "  \"email_subject\": \"string\",\n"
            "  \"email_body\": \"string\",\n"
            "  \"follow_up_strategy\": \"string\"\n"
            "}"
        ),
        output_json=True,
        tools=[get_sentiment_tool(), get_search_tool()],
        agent=agent,
        context=context_tasks
    )

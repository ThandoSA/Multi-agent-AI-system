from crewai import Agent
from config.llm import get_llm

def planner_agent():
    return Agent(
        role="Planner Angent",
        goal="Break complex problems into actionable steps.",
        backstory="You are an expert AI planner used in enterprise systems.",
        llm=get_llm(),
        verbose=True
    )
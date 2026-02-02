from crewai import Agent 
from config.llm import get_llm

def researcher_agent():
    return Agent(
        role="Researcher Agent",
        goal="Gather accurate and relevant information",
        backstory="You are a professional AI researcher.",
        llm=get_llm(),
        verbose=True
    )
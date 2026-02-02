from crewai import Agent
from config.llm import get_llm

def critic_agent():
    return Agent(
        role="Critic Agent",
        goal="Review and improve AI outputs for clarity and accuracy.",
        backstory="You ensure enterprise-grade quality control.",
        llm=get_llm(),
        verbose=True 
    )
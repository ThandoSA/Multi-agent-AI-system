from crewai import Task

def research_task(agent):
    return Task(
        description="Research the topic: Benefits of multi-agent AI systems in enterprises.",
        expected_output="Bullet-point research findings",
        agent=agent 
    )
from crewai import Task

def planning_task(agent):
    return Task(
        description="Create a structured plan based on the research",
        expected_output="Step-by-step execution plan",
        agent=agent
    )
    
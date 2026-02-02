from crewai import Task

def review_task(agent):
    return Task(
        description="Review and refine the final plan for clarity and completeness.",
        expected_output="Polished final response",
        agent=agent
    )
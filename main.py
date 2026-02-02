from crewai import Crew
from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.critic import critic_agent
from tasks.research_task import research_task 
from tasks.planning_task import planning_task
from tasks.review_task import review_task

planner = planner_agent()
researcher = researcher_agent()
critic = critic_agent()

crew = Crew(
    agents=[researcher, planner, critic],
    tasks=[
        research_task(researcher),
        planning_task(planner),
        review_task(critic)
    ],
    verbose=True
)

result = crew.kickoff()
print(result)
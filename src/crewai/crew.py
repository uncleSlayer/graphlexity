from crewai import Crew
from ..langgraph.state import AgentState
from .agents import Agents
from .tasks import Tasks
import json


class SearchCrew:

    def __init__(self):

        agents = Agents()

        self.sub_topic_finder_agent = agents.sub_topic_finder_agent()
        self.brave_search_agent = agents.brave_search_agent()

    def kickoff_sub_topics(self, state: AgentState) -> AgentState:

        tasks = Tasks()

        sub_topic_finding_task = tasks.sub_topic_finder_task(
            self.sub_topic_finder_agent, state["user_query"]
        )

        crew = Crew(
            agents=[self.sub_topic_finder_agent], tasks=[sub_topic_finding_task]
        )

        result = crew.kickoff()

        state["sub_topics_identified"] = json.loads(result.raw)["sub_topics"]

        return state

    def kickoff_brave_search(self, state: AgentState) -> AgentState:

        tasks = Tasks()

        brave_search_task = tasks.brave_search_task(
            self.brave_search_agent, state["sub_topics_identified"]
        )

        crew = Crew(agents=[self.brave_search_agent], tasks=[brave_search_task])

        result = crew.kickoff()

        state["brave_search_results"] = json.loads(result.raw)["web_pages"]

        return state

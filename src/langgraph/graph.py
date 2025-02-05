from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_community.tools import BraveSearch
import json
from .state import AgentState
from ..crewai.crew import SearchCrew


def register_query(state: AgentState) -> list[dict]:

    user_query = state["user_query"]

    state["user_query"] = user_query

    return state


class Node():

    def register_query(self, state: AgentState) -> list[dict]:

        user_query = state["user_query"]

        state["user_query"] = user_query

        # tool = BraveSearch.from_api_key(
        #     api_key="BSAKGb4s1B70r_nb8YKCuJU-zhuNqmP", search_kwargs={"count": 5}
        # )

        # result_str = tool.run(search_term)

        # result_deserialized = json.loads(result_str)

        # top_five_results = [
        #     {"title": result.title, "link": result.link, "snippet": result.snippet}
        #     for result in result_deserialized
        # ]

        return state


class WorkFlow:

    def __init__(self):

        graph = StateGraph(AgentState)

        nodes = Node()

        graph.add_node("register_query", nodes.register_query)

        graph.add_node("register_sub_topics", SearchCrew().kickoff_sub_topics)

        graph.add_node("register_brave_search", SearchCrew().kickoff_brave_search)

        graph.add_edge("register_query", "register_sub_topics")
        
        graph.add_edge("register_sub_topics", "register_brave_search")

        graph.set_entry_point("register_query")

        self.app = graph.compile()

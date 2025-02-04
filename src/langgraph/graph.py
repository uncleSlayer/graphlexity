from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_community.tools import BraveSearch
import json


class State(TypedDict):

    search_term: str


graph = StateGraph(State)


def search_on_brave(state: State):

    search_term = state["search_term"]

    tool = BraveSearch.from_api_key(
        api_key="BSAKGb4s1B70r_nb8YKCuJU-zhuNqmP", search_kwargs={"count": 5}
    )

    result_str = tool.run(search_term)

    result_deserialized = json.loads(result_str)

    top_five_results = [
        {"title": result.title, "link": result.link, "snippet": result.snippet}
        for result in result_deserialized
    ]

    return top_five_results


# graph.add_node("brave_search", search_on_brave())

from langgraph.graph import StateGraph
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

        return state


class WorkFlow:

    def __init__(self):

        graph = StateGraph(AgentState)

        nodes = Node()

        graph.add_node("register_query", nodes.register_query)

        graph.add_node("register_sub_topics", SearchCrew().kickoff_sub_topics)

        graph.add_node("register_brave_search", SearchCrew().kickoff_brave_search)

        graph.add_node("register_final_answer", SearchCrew().kickoff_final_answer)

        graph.add_edge("register_query", "register_sub_topics")
        
        graph.add_edge("register_sub_topics", "register_brave_search")

        graph.add_edge("register_brave_search", "register_final_answer")

        graph.set_entry_point("register_query")

        self.app = graph.compile()

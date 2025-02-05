from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    sub_topics_identified: list[str]
    brave_search_results: list[dict]
    final_answer: str

from textwrap import dedent
from crewai import Agent
from .tools import CustomTools


class Agents:

    def sub_topic_finder_agent(self):

        return Agent(
            name="sub_topic_finder_agent",
            role="Senior Sub Topic Finder",
            goal="Find sub topics for a user query",
            backstory=dedent(
                """
                You are a senior sub topic finder agent. You will be given a user query and you will return a list of sub topics that the user is interested in.
                You specialize in dividing up a user query into sub topics. You will return a list of sub topics that the user is interested in.
                The length of the sub topics list should be no more than 5 but random between 1 and 5.
                """
            ),
            verbose=True,
        )

    def brave_search_agent(self):
        return Agent(
            name="brave_search_agent",
            role="Brave Search Agent",
            goal="Find relevant web pages based on identified subtopics",
            backstory=dedent(
                """
                You are a Search agent. You will be given a list of subtopics and you will return a list of relevant web pages.
                You will use the search_brave_tool tool to find relevant web pages based on the subtopics.
                """
            ),
            tools=[CustomTools.search_brave_tool],
            verbose=True,
        )

    def final_answer_agent(self):
        return Agent(
            name="final_answer_writer_agent",
            role="Final Answer Agent",
            goal="Generate a final answer based on the user query, subtopics, and web pages",
            backstory=dedent(
                """
                You are an expert writer. You will be given a user query, subtopics, and web pages and you will return a final answer.
                You will use the final_answer_tool tool to generate a final answer based on the user query, subtopics, and web pages.
                """
            ),
            verbose=True,
        )

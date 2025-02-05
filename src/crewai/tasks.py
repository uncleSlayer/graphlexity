from crewai import Task
from textwrap import dedent
from pydantic import BaseModel


class sub_topic_finder_output(BaseModel):
    sub_topics: list[str]


class brave_search_output(BaseModel):
    web_pages: list[dict]


class Tasks:
    def sub_topic_finder_task(self, agent, query):

        return Task(
            description=dedent(
                f"""\
                Analyze a user query and generate a list of relevant subtopics, ensuring the list contains between 1 and 5 subtopics."

				USER QUERY
				-------
				{query}

				Your final answer MUST be a list of relevant subtopics, each subtopic MUST be a string, and the list MUST be no more than 5 subtopics.
				"""
            ),
            agent=agent,
            expected_output="a valid json list of subtopics",
            output_pydantic=sub_topic_finder_output,
        )

    def brave_search_task(self, agent, sub_topics):

        return Task(
            description=dedent(
                f"""\
                Use the Brave Search API to find relevant web pages based on identified subtopics.

				SUB TOPICS
				-------
				{sub_topics}

				Your final answer MUST be a list of relevant web page details.
				"""
            ),
            agent=agent,
            expected_output="a valid json list of web pages",
            output_pydantic=brave_search_output,
        )

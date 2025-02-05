from crewai import Task
from textwrap import dedent
from pydantic import BaseModel


class sub_topic_finder_output(BaseModel):
    sub_topics: list[str]


class brave_search_output(BaseModel):
    web_pages: list[dict]


class final_answer_output(BaseModel):
    final_answer: str


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

    def final_answer_task(self, agent, user_query, sub_topics, web_pages):

        return Task(
            description=dedent(
                f"""\
                Generate a final answer based on the user query, subtopics, and web pages.

                Some times web_pages or the subtopics may be empty, or may not be properly related to the user query.

                The priority of the final answer is to be relevant to the user query, and to be as concise as possible.

				USER QUERY
				-------
				{user_query}

				SUB TOPICS
				-------
				{sub_topics}

				WEB PAGES
				-------
				{web_pages}

				Your final answer MUST be a string.
				"""
            ),
            agent=agent,
            expected_output="a valid string",
            output_pydantic=final_answer_output,
        )

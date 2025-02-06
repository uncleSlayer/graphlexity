from langchain.tools import tool
import json
from pydantic import BaseModel
from langchain_community.tools import BraveSearch
import time
from config.env import settings as ENV_SETTINGS


class CustomToolSchema(BaseModel):
    queries: list[str]


class CustomTools:

    @tool("search_brave_tool", args_schema=CustomToolSchema)
    def search_brave_tool(queries: list[str]) -> list[dict]:
        """
        This tool uses the Brave Search API to find relevant web pages based on a list of subtopics.

        Args:
            queries (list[str]): A list of subtopics.

        Returns:
            str: A list of relevant web pages.
        """

        from langchain_community.utilities import GoogleSerperAPIWrapper

        try:

            response = []

            for query in queries:

                serper = GoogleSerperAPIWrapper()
                result = serper.results(query)

                first_organic_result = result.get("organic")[0]
                # time sleep is needed not to get rate limited by brave search
                time.sleep(2)

                response.append(
                    {
                        "title": first_organic_result['title'],
                        "link": first_organic_result['link'],
                        "snippet": first_organic_result['snippet']
                    }
                )

            return response

        except Exception as e:
            print(e)

            return "Error while searching"


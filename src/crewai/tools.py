from langchain.tools import tool
import json
from pydantic import BaseModel
from langchain_community.tools import BraveSearch
import time

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

        try:

            response = []

            brave = BraveSearch.from_api_key(
                api_key="BSAKGb4s1B70r_nb8YKCuJU-zhuNqmP", search_kwargs={"count": 1}
            )

            for query in queries:

                result_str = brave.run(query)

                # time sleep is needed not to get rate limited by brave search
                time.sleep(2)

                result_deserialized = json.loads(result_str)[0]

                response.append(
                    {
                        "title": result_deserialized['title'],
                        "link": result_deserialized['link'],
                        "snippet": result_deserialized['snippet']
                    }
                )

            return response

        except Exception as e:
            print(e)

            return "Error while searching"

        # for query in query_list:

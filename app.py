from fastapi import FastAPI
from dotenv import load_dotenv
from src.langgraph.graph import WorkFlow
from pydantic import BaseModel
from config.env import settings as ENV_SETTINGS

load_dotenv()

app = FastAPI()


class Query(BaseModel):
    query: str


@app.post("/search")
def read_root(query: Query):

    user_query = query.query

    workflow = WorkFlow()

    ans = workflow.app.invoke(
        {
            "user_query": user_query,
            "sub_topics_identified": [],
            "brave_search_results": [],
            "final_answer": "",
        }
    )

    return {"result": ans}


@app.get("/health-check")
def health_check():
    from langchain_community.tools import BraveSearch
    from langchain_community.utilities import GoogleSerperAPIWrapper

    brave = GoogleSerperAPIWrapper()
    result = brave.results("who is the prime minister of India?")
    return {"status": result.get("organic")[0]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

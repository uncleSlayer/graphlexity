from fastapi import FastAPI
from dotenv import load_dotenv
# from src.langgraph.graph import register_query
from src.langgraph.graph import WorkFlow
# from .src.langgraph.state import AgentState
from pydantic import BaseModel


load_dotenv()

app = FastAPI()


class Query(BaseModel):
    query: str

@app.post("/search")
def read_root(query: Query):

    user_query = query.query

    workflow = WorkFlow()

    ans = workflow.app.invoke({
        "user_query": user_query,
        "sub_topics_identified": [],
        "brave_search_results": [],
        "final_answer": ""
    })

    return {"result": ans}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

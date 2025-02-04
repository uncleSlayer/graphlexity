from fastapi import FastAPI
from dotenv import load_dotenv
from src.langgraph.graph import search_on_brave

load_dotenv()

app = FastAPI()


@app.get("/health")
def read_root():
    ans = search_on_brave({"search_term": "who is the prime minister of India?"})
    return {"health": "ok!", "result": ans}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
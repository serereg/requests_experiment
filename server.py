import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q1: int = None, q2: int = None):
    return {"item_id": item_id, "q1": q1, "q2": q2}


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info")

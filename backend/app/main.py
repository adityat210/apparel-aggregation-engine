from fastapi import FastAPI

app = FastAPI(title="Apparel Aggregation Engine API")

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "running Apparel Aggregation Engine API"}
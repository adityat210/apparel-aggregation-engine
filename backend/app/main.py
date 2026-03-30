from fastapi import FastAPI

from app.models.product import Product
from app.schemas.product import ProductResponse

app = FastAPI(title="Apparel Aggregation Engine API")


@app.get("/")
def read_root() -> dict[str,str]:
    return {"message": "running Apparel Aggregation Engine API"}






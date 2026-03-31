from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.base import Base
from app.db.dependencies import get_db
from app.db.session import engine
from app.models.product import Product

import app.db.init_db  # noqa: F401

app = FastAPI(title="Apparel Aggregation Engine API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "currently running Apparel Aggregation Engine API"}


@app.get("/products/count")
def get_product_count(db: Session = Depends(get_db)) -> dict[str, int]:
    count = db.query(Product).count()
    return {"count": count}
from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.base import Base
from app.db.dependencies import get_db
from app.db.session import engine
from app.models.product import Product
from app.schemas.product import ProductResponse
from typing import List, Optional

import app.db.init_db

app = FastAPI(title="Apparel Aggregation Engine API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "currently running Apparel Aggregation Engine API"}


@app.get("/products/count")
def get_product_count(db: Session = Depends(get_db)) -> dict[str, int]:
    count = db.query(Product).count()
    return {"count": count}

@app.get("/products", response_model=List[ProductResponse])
def get_products(
    retailer: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock: Optional[bool] = None,
    db: Session = Depends(get_db),
) -> list[Product]:
    products = db.query(Product).all()
    return products
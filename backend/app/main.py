from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy import desc
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
    sort_by: Optional[str] = None,
    max_price: Optional[float] = None,
    in_stock: Optional[bool] = None,
    db: Session = Depends(get_db),
) -> list[Product]:
    query = db.query(Product) #start with all products
    #filters narrow query only if user provided that filter
    #no query parameters = all products returned
    if retailer is not None:
        query = query.filter(Product.retailer == retailer)
    if category is not None:
        query = query.filter(Product.category == category)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if in_stock is not None:
        query = query.filter(Product.in_stock == in_stock)

    #sort by price ascending, price descending, or rating descending if provided sort_by
    if sort_by == "price_asc":
        query = query.order_by(Product.price)
    elif sort_by == "price_desc":
        query = query.order_by(desc(Product.price))
    elif sort_by == "rating_desc":
        query = query.order_by(desc(Product.rating))

    products = query.all()
    return products
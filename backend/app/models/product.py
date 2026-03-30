from typing import Optional

from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True) #internal database ID
    retailer: Mapped[str] = mapped_column(String, nullable=False) #every product has a retailer
    external_id: Mapped[str] = mapped_column(String, nullable=False) #ID that came from the retailer's source
    name: Mapped[str] = mapped_column(String, nullable=False) #every product has a name
    brand: Mapped[Optional[str]] = mapped_column(String, nullable=True) #brand is optional
    category: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    color: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False) #price is required 
    currency: Mapped[str] = mapped_column(String, nullable=False, default="USD")
    material: Mapped[Optional[str]] = mapped_column(String, nullable=True) #material is optional
    image_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    product_url: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    review_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    in_stock: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
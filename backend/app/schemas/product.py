from typing import Optional

from pydantic import BaseModel, ConfigDict
#schemas for the API layer, not the database itself


#common product fields schema
class ProductBase(BaseModel):
    retailer: str
    external_id: str
    name: str
    brand: Optional[str] = None
    category: Optional[str] = None
    color: Optional[str] = None
    price: float
    currency: str = "USD"
    material: Optional[str] = None
    image_url: Optional[str] = None
    product_url: str
    rating: Optional[float] = None
    review_count: Optional[int] = None
    in_stock: bool = True

#what we could accept when creating a product
class ProductCreate(ProductBase):
    pass

#what we send back in API responses
class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
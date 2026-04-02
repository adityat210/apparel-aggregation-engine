from typing import Any
#file converts source-specific records into one product shape
#both retailers produce data that fits into Product model
def normalize_retailer_a_product(raw_product: dict[str, Any]) -> dict[str, Any]:
    return {
        "retailer": "retailer_a",
        "external_id": raw_product["id"],
        "name": raw_product["title"],
        "brand": raw_product.get("brand"),
        "category": raw_product.get("category"),
        "color": raw_product.get("color"),
        "price": float(raw_product["price_usd"]),
        "currency": "USD",
        "material": raw_product.get("material"),
        "image_url": raw_product.get("image"),
        "product_url": raw_product["url"],
        "rating": raw_product.get("rating"),
        "review_count": raw_product.get("reviews"),
        "in_stock": raw_product.get("in_stock", True),
    }

def normalize_retailer_b_product(raw_product: dict[str, Any]) -> dict[str, Any]:
    return {
        "retailer": "retailer_b",
        "external_id": raw_product["sku"],
        "name": raw_product["name"],
        "brand": raw_product.get("maker"),
        "category": raw_product.get("type"),
        "color": raw_product.get("shade"),
        "price": float(raw_product["price"]),
        "currency": "USD",
        "material": raw_product.get("fabric"),
        "image_url": raw_product.get("image_url"),
        "product_url": raw_product["product_link"],
        "rating": raw_product.get("stars"),
        "review_count": raw_product.get("review_count"),
        "in_stock": raw_product.get("available", True),
    }
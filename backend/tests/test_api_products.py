from fastapi.testclient import TestClient

from app.main import app
from ingestion.refresh import refresh_product_data

client = TestClient(app)

def setup_module(module) -> None:
    refresh_product_data()

def test_products_count_route() -> None:
    response = client.get("/products/count")

    assert response.status_code == 200

    products = response.json()
    assert products == {"count": 18}

def test_products_route_filters_by_retailer() -> None:
    response = client.get("/products?retailer=retailer_a")

    assert response.status_code == 200

    products = response.json()
    assert len(products) == 3
    for product in products:
        assert product["retailer"] == "retailer_a"

def test_products_route_filters_by_category() -> None:
    response = client.get("/products?category=tops")
    assert response.status_code == 200

    products = response.json()
    assert len(products) == 6
    for product in products:
        assert product["category"] == "tops"

def test_products_route_sorts_by_price_ascending() -> None:
    response = client.get("/products?sort_by=price_asc")
    assert response.status_code == 200

    products = response.json()
    prices = [product["price"] for product in products]

    assert prices == sorted(prices)
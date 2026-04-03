from ingestion.normalize import(
    normalize_retailer_a_product,
    normalize_retailer_b_product
)
    
def test_normalize_retailer_a_product():
    raw_product = {
        "id": "a-101",
        "title": "Classic Cotton T-Shirt",
        "brand": "Northline",
        "category": "tops",
        "color": "blue",
        "price_usd": 24.99,
        "material": "100% cotton",
        "image": "https://example.com/images/a101.jpg",
        "url": "https://example.com/products/a101",
        "rating": 4.4,
        "reviews": 120,
        "in_stock": True
    }

    normalized_product = normalize_retailer_a_product(raw_product)

    assert normalized_product["retailer"] == "retailer_a"
    assert normalized_product["external_id"] == "a-101"
    assert normalized_product["name"] == "Classic Cotton T-Shirt"
    assert normalized_product["brand"] == "Northline"
    assert normalized_product["category"] == "tops"
    assert normalized_product["color"] == "blue"
    assert normalized_product["price"] == 24.99
    assert normalized_product["currency"] == "USD"
    assert normalized_product["material"] == "100% cotton"
    assert normalized_product["image_url"] == "https://example.com/images/a101.jpg"
    assert normalized_product["product_url"] == "https://example.com/products/a101"
    assert normalized_product["rating"] == 4.4
    assert normalized_product["review_count"] == 120
    assert normalized_product["in_stock"] is True

def test_normalize_retailer_b_product() -> None:
    raw_product = {
        "sku": "b-201",
        "name": "Soft Knit Sweater",
        "maker": "Urban Coast",
        "type": "tops",
        "shade": "cream",
        "price": "44.00",
        "fabric": "acrylic",
        "image_url": "https://example.com/images/b201.jpg",
        "product_link": "https://example.com/products/b201",
        "stars": 4.1,
        "review_count": 48,
        "available": True,
    }

    normalized_product = normalize_retailer_b_product(raw_product)

    assert normalized_product["retailer"] == "retailer_b"
    assert normalized_product["external_id"] == "b-201"
    assert normalized_product["name"] == "Soft Knit Sweater"
    assert normalized_product["brand"] == "Urban Coast"
    assert normalized_product["category"] == "tops"
    assert normalized_product["color"] == "cream"
    assert normalized_product["price"] == 44.0
    assert normalized_product["currency"] == "USD"
    assert normalized_product["material"] == "acrylic"
    assert normalized_product["image_url"] == "https://example.com/images/b201.jpg"
    assert normalized_product["product_url"] == "https://example.com/products/b201"
    assert normalized_product["rating"] == 4.1
    assert normalized_product["review_count"] == 48
    assert normalized_product["in_stock"] is True
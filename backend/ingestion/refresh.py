from app.models.product import Product
from app.db.session import SessionLocal
from ingestion.adapters.retailer_a import load_retailer_a_products
from ingestion.adapters.retailer_b import load_retailer_b_products
from ingestion.adapters.retailer_c import load_retailer_c_products
from ingestion.adapters.retailer_d import load_retailer_d_products
from ingestion.adapters.retailer_e import load_retailer_e_products
from ingestion.adapters.retailer_f import load_retailer_f_products
from ingestion.normalize import (
    normalize_retailer_a_product,
    normalize_retailer_b_product,
    normalize_retailer_c_product,
    normalize_retailer_d_product,
    normalize_retailer_e_product,
    normalize_retailer_f_product
)


def refresh_product_data() -> None:
    db = SessionLocal()

    try:
        db.query(Product).delete()

        retailer_a_products = load_retailer_a_products()
        retailer_b_products = load_retailer_b_products()
        retailer_c_products = load_retailer_c_products()
        retailer_d_products = load_retailer_d_products()
        retailer_e_products = load_retailer_e_products()
        retailer_f_products = load_retailer_f_products()

        normalized_products = []

        for raw_product in retailer_a_products:
            normalized_products.append(normalize_retailer_a_product(raw_product))

        for raw_product in retailer_b_products:
            normalized_products.append(normalize_retailer_b_product(raw_product))

        for raw_product in retailer_c_products:
            normalized_products.append(normalize_retailer_c_product(raw_product))

        for raw_product in retailer_d_products:
            normalized_products.append(normalize_retailer_d_product(raw_product))

        for raw_product in retailer_e_products:
            normalized_products.append(normalize_retailer_e_product(raw_product))

        for raw_product in retailer_f_products:
            normalized_products.append(normalize_retailer_f_product(raw_product))

        for product_data in normalized_products:
            product = Product(**product_data)
            db.add(product)

        db.commit()

    finally:
        db.close()

if __name__ == "__main__":
    refresh_product_data()
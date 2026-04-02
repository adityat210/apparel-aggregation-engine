from app.models.product import Product
from app.db.session import SessionLocal
from ingestion.adapters.retailer_a import load_retailer_a_products
from ingestion.adapters.retailer_b import load_retailer_b_products
from ingestion.normalize import (
    normalize_retailer_a_product,
    normalize_retailer_b_product,
)


def refresh_product_data() -> None:
    db = SessionLocal()

    try:
        print("Starting refresh...")

        deleted_count = db.query(Product).delete()
        print(f"Deleted existing products: {deleted_count}")

        retailer_a_products = load_retailer_a_products()
        retailer_b_products = load_retailer_b_products()
        print(f"Loaded raw products -> retailer_a: {len(retailer_a_products)}, retailer_b: {len(retailer_b_products)}")

        normalized_products = []

        for raw_product in retailer_a_products:
            normalized_products.append(normalize_retailer_a_product(raw_product))

        for raw_product in retailer_b_products:
            normalized_products.append(normalize_retailer_b_product(raw_product))

        print(f"Normalized products: {len(normalized_products)}")

        for product_data in normalized_products:
            product = Product(**product_data)
            db.add(product)

        db.commit()
        print("Refresh committed successfully.")

        final_count = db.query(Product).count()
        print(f"Final product count in database: {final_count}")

    finally:
        db.close()


if __name__ == "__main__":
    refresh_product_data()
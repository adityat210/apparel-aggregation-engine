from app.db.session import SessionLocal
from app.models.product import Product
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
    normalize_retailer_f_product,
)


def refresh_product_data() -> None:
    db = SessionLocal()

    retailer_configs = [
        ("retailer_a", load_retailer_a_products, normalize_retailer_a_product),
        ("retailer_b", load_retailer_b_products, normalize_retailer_b_product),
        ("retailer_c", load_retailer_c_products, normalize_retailer_c_product),
        ("retailer_d", load_retailer_d_products, normalize_retailer_d_product),
        ("retailer_e", load_retailer_e_products, normalize_retailer_e_product),
        ("retailer_f", load_retailer_f_products, normalize_retailer_f_product),
    ]

    try:
        db.query(Product).delete()

        for retailer_name, load_fn, normalize_fn in retailer_configs:
            try:
                raw_products = load_fn()
            except Exception as error:
                print(f"Didn't load products for {retailer_name}: {error}")
                continue

            for raw_product in raw_products:
                try:
                    normalized_product = normalize_fn(raw_product)
                    product = Product(**normalized_product)
                    db.add(product)
                except Exception as error:
                    print(
                        f"skipping invalid product from {retailer_name}: "
                        f"{raw_product}. Error: {error}"
                    )
                    continue

        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    refresh_product_data()
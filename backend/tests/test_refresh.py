from app.db.session import SessionLocal
from app.models.product import Product
from ingestion.refresh import refresh_product_data

def test_refresh_product_data_inserts_expected_products() -> None:
    db = SessionLocal()

    try:
        # clear
        db.query(Product).delete()
        db.commit()

        starting_count = db.query(Product).count()
        assert starting_count == 0

        # refresh
        refresh_product_data()

        #validate data
        final_count = db.query(Product).count()
        assert final_count == 18 

    finally:
        db.close()
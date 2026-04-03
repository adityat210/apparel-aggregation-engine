from app.db.session import SessionLocal
from app.models.product  import Product
from ingestion.refresh import refresh_product_data

def test_refresh_product_data_inserts_expected_products() -> None:
    db = SessionLocal()

    try:
        #deletes any exsisting products
        db.query(Product).delete()
        db.commit()

        starting_count = db.query(Product).count()
        assert starting_count == 0 #confirms table starts at 0


    finally:
        db.close()
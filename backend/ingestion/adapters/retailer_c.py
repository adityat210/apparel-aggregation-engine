import json
from pathlib import Path

def load_retailer_c_products() -> list[dict]:
   
    file_path = Path(__file__).resolve().parent.parent / 'sample_data' / 'retailer_c_products.json'
    with open(file_path, 'r') as f:
        products = json.load(f)
    return products
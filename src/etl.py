import json
from transform import transform_property_record
from db import DBConnection
from utils import log_info, log_error


RAW_JSON_PATH ="E:\\data_engineer_assessment Sudarshan D\\data\\fake_property_data_new.json"  

def load_raw_json(path):
    """Read raw JSON file"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        log_info(f"Loaded {len(data)} records from raw JSON")
        return data
    except Exception as e:
        log_error(f"Error loading JSON: {e}")
        return []


def insert_raw_json(db, record):
    """Insert raw JSON into raw_data table"""
    try:
        query = """
            INSERT INTO raw_data (raw_json)
            VALUES (%s)
        """
        db.execute(query, (json.dumps(record),))
    except Exception as e:
        log_error(f"Failed inserting raw record: {e}")


def insert_property(db, prop):
    """Insert into properties table"""
    query = """
        INSERT INTO properties (
            raw_property_id, address, city, state, zipcode,
            bedrooms, bathrooms, sqft, lot_size, year_built
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (
        prop["raw_property_id"], prop["address"], prop["city"], prop["state"],
        prop["zipcode"], prop["bedrooms"], prop["bathrooms"], prop["sqft"],
        prop["lot_size"], prop["year_built"]
    )
    return db.execute_and_return_id(query, values)


def insert_hoa(db, prop_id, hoa):
    if hoa is None:
        return

    query = """
        INSERT INTO hoa_details (
            property_id, hoa_fee, hoa_frequency, hoa_contact
        ) VALUES (%s, %s, %s, %s)
    """
    values = (prop_id, hoa["hoa_fee"], hoa["hoa_frequency"], hoa["hoa_contact"])
    db.execute(query, values)


def insert_rehab(db, prop_id, rehab):
    if rehab is None:
        return

    query = """
        INSERT INTO rehab_estimates (
            property_id, estimated_cost, description, contractor_name
        ) VALUES (%s, %s, %s, %s)
    """
    values = (
        prop_id, rehab["estimated_cost"], rehab["description"], rehab["contractor_name"]
    )
    db.execute(query, values)


def insert_valuation(db, prop_id, valuation):
    if valuation is None:
        return

    query = """
        INSERT INTO valuations (
            property_id, market_value, as_is_value, arv_value, valuation_date
        ) VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        prop_id, valuation["market_value"], valuation["as_is_value"],
        valuation["arv_value"], valuation["valuation_date"]
    )
    db.execute(query, values)


def process_record(db, record):
    """Process one raw record end-to-end"""
    # 1. Insert raw JSON
    insert_raw_json(db, record)

    # 2. Transform JSON → normalized dicts
    prop, hoa, rehab, valuation = transform_property_record(record)

    # 3. Insert main property and receive property_id
    prop_id = insert_property(db, prop)

    # 4. Insert related tables
    insert_hoa(db, prop_id, hoa)
    insert_rehab(db, prop_id, rehab)
    insert_valuation(db, prop_id, valuation)


def run_etl():
    """Run full ETL pipeline"""
    db = DBConnection()

    records = load_raw_json(RAW_JSON_PATH)

    for r in records:
        process_record(db, r)

    log_info("ETL completed successfully!")


if __name__ == "__main__":
    run_etl()

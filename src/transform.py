from utils import log_info, log_error

def safe_get(record, key, default=None):
    return record.get(key, default)

def clean_number(value):
    try:
        if value in (None, "", "null", "NaN"):
            return None
        return float(value)
    except:
        return None

def clean_string(value):
    if value is None:
        return None
    value = str(value).strip()
    return value if value != "" else None

def transform_property_record(record):
    try:
        property_dict = {
            "raw_property_id": safe_get(record, "id"),
            "address": clean_string(safe_get(record, "address")),
            "city": clean_string(safe_get(record, "city")),
            "state": clean_string(safe_get(record, "state")),
            "zipcode": clean_string(safe_get(record, "zipcode")),
            "bedrooms": clean_number(safe_get(record, "bedrooms")),
            "bathrooms": clean_number(safe_get(record, "bathrooms")),
            "sqft": clean_number(safe_get(record, "sqft")),
            "lot_size": clean_number(safe_get(record, "lot_size")),
            "year_built": clean_number(safe_get(record, "year_built")),
        }

        if "hoa" in record and record["hoa"]:
            hoa = record["hoa"]
            hoa_dict = {
                "hoa_fee": clean_number(hoa.get("fee")),
                "hoa_frequency": clean_string(hoa.get("frequency")),
                "hoa_contact": clean_string(hoa.get("contact")),
            }
        else:
            hoa_dict = None

        if "rehab" in record and record["rehab"]:
            rehab = record["rehab"]
            rehab_dict = {
                "estimated_cost": clean_number(rehab.get("estimate")),
                "description": clean_string(rehab.get("description")),
                "contractor_name": clean_string(rehab.get("contractor")),
            }
        else:
            rehab_dict = None

        if "valuation" in record and record["valuation"]:
            val = record["valuation"]
            valuation_dict = {
                "market_value": clean_number(val.get("market")),
                "as_is_value": clean_number(val.get("asis")),
                "arv_value": clean_number(val.get("arv")),
                "valuation_date": clean_string(val.get("date")),
            }
        else:
            valuation_dict = None

        return property_dict, hoa_dict, rehab_dict, valuation_dict

    except Exception as e:
        log_error(f"Transform failed: {e}")
        return None, None, None, None

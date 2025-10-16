def serialize_json(data):
    import json
    return json.dumps(data)

def deserialize_json(data):
    import json
    return json.loads(data)

def validate_stock_symbol(symbol):
    if not isinstance(symbol, str) or len(symbol) == 0:
        raise ValueError("Invalid stock symbol. It must be a non-empty string.")
    return symbol.upper()  # Return the symbol in uppercase for consistency

def format_date(date):
    from datetime import datetime
    return datetime.strptime(date, "%Y-%m-%d").date() if date else None

def calculate_percentage_change(old_value, new_value):
    if old_value == 0:
        raise ValueError("Old value cannot be zero for percentage change calculation.")
    return ((new_value - old_value) / old_value) * 100
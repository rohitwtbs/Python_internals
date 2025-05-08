import json
from collections import defaultdict


data = defaultdict(list)
def serialize(obj):
    if isinstance(obj, defaultdict):
        return {key: serialize(value) for key, value in obj.items()}
    elif hasattr(obj, "__dict__"):  # For objects with __dict__ attribute
        return {key: serialize(value) for key, value in obj.__dict__.items()}
    elif isinstance(obj, list):  # For lists
        return [serialize(item) for item in obj]
    elif isinstance(obj, dict):  # For dictionaries
        return {key: serialize(value) for key, value in obj.items()}
    else:
        return obj  # Return the value as is for primitive types


serialized_data = serialize(data)

print(json.dumps(serialized_data, indent=4))
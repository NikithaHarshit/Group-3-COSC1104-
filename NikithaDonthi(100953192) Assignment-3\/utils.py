import requests

def fetch_cost_data():
    """
    Fetch cost data from cloud provider APIs (mock example).
    Returns:
        list: A list of cost data dictionaries.
    """
    return [
        {"service": "Compute Engine", "cost": 150.00},
        {"service": "Cloud Storage", "cost": 90.50},
        {"service": "BigQuery", "cost": 120.25},
    ]

def analyze_costs(data):
    """
    Analyze cost data to calculate total and breakdowns.
    Args:
        data (list): List of service cost dictionaries.
    Returns:
        dict: Analysis summary including total cost.
    """
    total = sum(item['cost'] for item in data)
    return {"total_cost": total, "details": data}

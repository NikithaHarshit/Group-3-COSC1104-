import matplotlib.pyplot as plt

def generate_report(data):
    """
    Generate a bar chart report for cloud costs.
    Args:
        data (dict): Analyzed cost data.
    """
    services = [item['service'] for item in data['details']]
    costs = [item['cost'] for item in data['details']]

    plt.bar(services, costs, color='skyblue')
    plt.title(f"Cloud Costs Report - Total: ${data['total_cost']:.2f}")
    plt.ylabel("Cost ($)")
    plt.savefig("cost_report.png")

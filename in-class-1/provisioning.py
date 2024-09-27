# provisioning.py
# Group member name: Harshit Sonik (100941462)
# Group member name: Nikitha Donthi (100953192)
# Date: 27-09-2024
# Description: Based on user input and available resources, this script simulates the provisioning of cloud resources.

# constants:
TOTAL_CPUCORES = 20 
TOTAL_MEMORYGB = 128.0

# validate input (BONUS):
def get_valid_input(prompt, value_type):
    while True:
        try:
            value = value_type(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# Get user inputs:
required_cpucores = get_valid_input("How many CPU cores do you need? ", int)
required_memorygb = get_valid_input("How much memory (in GB) do you need? ", float)

# if the requested resources are available or not:
if required_cpucores <= TOTAL_CPUCORES and required_memorygb <= TOTAL_MEMORYGB:
    print("Resources provisioned successfully.")
    TOTAL_CPUCORES -= required_cpucores
    TOTAL_MEMORYGB -= required_memorygb
else:
    print("Resource request exceeds capacity. Provisioning failed.")

#show remaining resources:
print(f"Remaining CPU cores: {TOTAL_CPUCORES}")
print(f"Remaining memory (GB): {TOTAL_MEMORYGB}")


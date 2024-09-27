# provisioning_loops.py
# Group Members: Nikitha Donthi, Harshit Sonik
# Date: 27-09-2024
# Description: A simple script to simulate cloud resource provisioning.

# constants:
Total_CPU_Cores = 20 
Total_Memory_GB = 128.0

# remaining capacity
remaining_cpucores = Total_CPU_Cores
remaining_memorygb = Total_Memory_GB

# allocated resources and pending requests
allocated_resources = list()
pending_requests = list()

# Continuously accept user requests
is_continuing = "yes"  # Variable to control the loop

while is_continuing.lower() == "yes":
    # user resource details
    username = input("username: ")
    requested_cpucores = int(input("How many CPU cores do you need? "))
    requested_memorygb = float(input("How much memory (in GB) do you need? "))

    # if the resources can be provisioned
    if requested_cpucores <= remaining_cpucores and requested_memorygb <= remaining_memorygb:
        allocated_resources.append([username, requested_cpucores, requested_memorygb])
        remaining_cpucores -= requested_cpucores
        remaining_memorygb -= requested_memorygb
    else:
        pending_requests.append([username, requested_cpucores, requested_memorygb])

    # user wants to make another request
    is_continuing = input("Do you want to make another request? (yes/no): ")

# After loop ends, display the results
print("\nAllocated Resources:")
for resource in allocated_resources:
    print(f"User: {resource[0]}, CPU cores: {resource[1]}, Memory (GB): {resource[2]}")

print("\nPending Requests:")
for request in pending_requests:
    print(f"User: {request[0]}, CPU cores: {request[1]}, Memory (GB): {request[2]}")
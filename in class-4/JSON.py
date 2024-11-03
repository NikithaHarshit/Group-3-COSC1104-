# JSON.py
# Group member name: Harshit Sonik (100941462)
# Group member name: Nikitha Donthi (100953192)
# Date: 02-11-2024
# Description: Create a console-based application to filter and display AWS EC2 instance types based on user-specified CPU and memory requirements using JSON data.

#1)	Get a valid minimum (and maximum) requirement for CPU cores from the user
#2)	Get a valid minimum (and maximum) requirement for memory from the user.

def get_input(prompt, value_type, allow_skip=False):
    while True:
        user_input = input(prompt)
        if allow_skip and user_input == "":
            return None
        try:
            return value_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {value_type.__name__}.")

min_cpu = get_input("Enter minimum CPU cores required: ", int)
max_cpu = get_input("Enter maximum CPU cores (press Enter to skip): ", int, allow_skip=True)
min_memory = get_input("Enter minimum memory required in GiB: ", float)
max_memory = get_input("Enter maximum memory (press Enter to skip): ", float, allow_skip=True)

#3)	Access the .json file containing the list of EC2 instance types.
import json

# Load the JSON data from the file
with open('C:\\Users\\nikit\\in-class 4\\ec2_instance_types.json', 'r') as file:
    ec2_instances = json.load(file)


#4)	Get the EC2 instance types as either a list of objects or as a dictionary.

def parse_vcpu(vcpu_str):
    # Extract the integer value of vCPUs
    return int(vcpu_str.split()[0])

def parse_memory(memory_str):
    # Extract the float value of memory in GiB
    return float(memory_str.split()[0])

# Normalize data in each instance
for instance in ec2_instances:
    instance['vcpu'] = parse_vcpu(instance['vcpu'])
    instance['memory'] = parse_memory(instance['memory'])


#Filter the EC2 Instances Based on User Criteria:

def filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory):
    filtered = []
    for instance in instances:
        if (min_cpu <= instance['vcpu'] and (max_cpu is None or instance['vcpu'] <= max_cpu)) and \
           (min_memory <= instance['memory'] and (max_memory is None or instance['memory'] <= max_memory)):
            filtered.append(instance)
    return filtered

matching_instances = filter_instances(ec2_instances, min_cpu, max_cpu, min_memory, max_memory)

#5) Display the Filtered Instances:
if matching_instances:
    print("\nMatching EC2 Instances:\n")
    for idx, instance in enumerate(matching_instances, start=1):
        print(f"{idx}. Name: {instance['name']}")
        print(f"   vCPUs: {instance['vcpu']}")
        print(f"   Memory: {instance['memory']} GiB")
        print("-" * 40)
else:
    print("No EC2 instances meet your specified criteria.")



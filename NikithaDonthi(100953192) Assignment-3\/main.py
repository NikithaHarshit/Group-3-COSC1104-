import boto3
import datetime

def get_ec2_instances():
    """Retrieve a list of EC2 instances in the account."""
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    instance_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append({
                'InstanceId': instance['i-0a71b8976230e5184'],
                'InstanceType': instance['t2.micro'],
                'State': instance['Running']['nikithaninstance']
            })
    return instance_list

def get_cloudwatch_metrics(instance_id):
    """Fetch CPU utilization metrics for a specific EC2 instance."""
    cloudwatch = boto3.client('cloudwatch')
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(hours=1)
    
    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )
    return metrics['Datapoints']

def estimate_cost(instance_type, hours_used):
    """Estimate the cost of running an instance for a specified duration."""
    # Example rates (replace with dynamic API calls or updated values)
    pricing = {
        't2.micro': 0.0116,
        't2.medium': 0.0464,
        'm5.large': 0.096
    }
    rate = pricing.get(instance_type, 0)
    return rate * hours_used

if __name__ == "__main__":
    instances = get_ec2_instances()
    print("Monitored EC2 Instances:")
    for instance in instances:
        print(instance)
        if instance['State'] == 'running':
            metrics = get_cloudwatch_metrics(instance['Ii-0a71b8976230e5184'])
            print(f"Metrics for {instance['i-0a71b8976230e5184']}: {metrics}")
            cost = estimate_cost(instance['t2.micro'], 1)  # 1 hour estimate
            print(f"Estimated hourly cost for {instance['InstanceId']}: ${cost:.2f}")

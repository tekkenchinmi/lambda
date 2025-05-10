# EC2 Start and Stop Lambda Function
'''
import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:auto-start-stop', 'Values': ['yes']}]
    )

    for instance in instances:
        if instance.state['Name'] == 'stopped':
            instance.start()
            print(f'Started instance: {instance.id}')
        elif instance.state['Name'] == 'running':
            instance.stop()
            print(f'Stopped instance: {instance.id}')
'''
# EC2 Start Script

import boto3
import unittest
from unittest.mock import patch

class EC2Manager:
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def start_instance(self, instance_id):
        response = self.ec2.start_instances(InstanceIds=[instance_id])
        return response

class TestEC2Manager(unittest.TestCase):
    @patch('boto3.client')
    def test_start_instance(self, mock_boto_client):
        mock_ec2 = mock_boto_client.return_value
        mock_ec2.start_instances.return_value = {'StartingInstances': [{'InstanceId': 'i-1234567890abcdef0', 'CurrentState': {'Name': 'pending'}}]}
        
        ec2_manager = EC2Manager()
        response = ec2_manager.start_instance('i-1234567890abcdef0')
        
        self.assertEqual(response['StartingInstances'][0]['InstanceId'], 'i-1234567890abcdef0')
        self.assertEqual(response['StartingInstances'][0]['CurrentState']['Name'], 'pending')

if __name__ == '__main__':
    unittest.main()


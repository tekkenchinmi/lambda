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
'''
# EC2 Start and Stop Lambda Function Unit Test

import unittest
from unittest.mock import patch, MagicMock
import boto3
from botocore.exceptions import ClientError

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.resource')
    def test_start_stopped_instance(self, mock_boto):
        # Arrange
        mock_instance = MagicMock()
        mock_instance.state = {'Name': 'stopped'}
        mock_instance.id = 'i-1234567890abcdef0'
        mock_boto.return_value.instances.filter.return_value = [mock_instance]

        # Act
        from your_lambda_module import lambda_handler
        lambda_handler({}, {})

        # Assert
        mock_instance.start.assert_called_once()
        print.assert_called_with('Started instance: i-1234567890abcdef0')

    @patch('boto3.resource')
    def test_stop_running_instance(self, mock_boto):
        # Arrange
        mock_instance = MagicMock()
        mock_instance.state = {'Name': 'running'}
        mock_instance.id = 'i-0987654321fedcba0'
        mock_boto.return_value.instances.filter.return_value = [mock_instance]

        # Act
        from your_lambda_module import lambda_handler
        lambda_handler({}, {})

        # Assert
        mock_instance.stop.assert_called_once()
        print.assert_called_with('Stopped instance: i-0987654321fedcba0')

    @patch('boto3.resource')
    def test_no_instances(self, mock_boto):
        # Arrange
        mock_boto.return_value.instances.filter.return_value = []

        # Act
        from your_lambda_module import lambda_handler
        lambda_handler({}, {})

        # Assert
        print.assert_not_called()

    @patch('boto3.resource')
    def test_client_error_handling(self, mock_boto):
        # Arrange
        mock_boto.side_effect = ClientError(
            {"Error": {"Code": "InvalidInstanceID.NotFound", "Message": "The instance ID does not exist."}},
            'StartInstances'
        )

        # Act
        from your_lambda_module import lambda_handler
        lambda_handler({}, {})

        # Assert
        print.assert_called_with('Error starting instance: InvalidInstanceID.NotFound')

if __name__ == '__main__':
    unittest.main()



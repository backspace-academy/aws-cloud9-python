# Load the AWS SDK for Python
import boto3

# Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError

# Create SQS client and set region
sqs = boto3.client('sqs', region_name='us-east-1')


# Main program
def main():
    print('Code loaded successfully')

if __name__ == '__main__':
    main()

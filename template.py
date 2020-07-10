# Load the AWS SDK for Python
import boto3

# Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError

# Create AWS service client and set region
s3 = boto3.client('s3', region_name='us-east-1')


# Main program
def main():
    print('Code loaded successfully')

if __name__ == '__main__':
    main()

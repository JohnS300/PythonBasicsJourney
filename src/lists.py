"""Create a list of AWS services and modify the list appropriately"""

def main():
    aws_services =['S3','Lamda','EC2','DynamoDB']
    
    print(f"AWS Services List: {aws_services}")
    first_item = aws_services[0]
    print(f"First service: {first_item}")
    last_item = aws_services[-1]
    print(f"Last service: {last_item}")
    
    
    aws_services[-1]= 'SNS'
    print(f"Last service: {aws_services}")

    #Add value at the end of the list
    aws_services.append('DynamoDB')
    aws_services.append('SQS')
    print(f"Updated AWS Services List: {aws_services}")

    #Remove value from a part of the list
    aws_services.pop(1)
    print(f"Updated AWS Services List: {aws_services}")

    #Slice the list to get services from index 1 to 3 , exclusive of 3
    sliced_services = aws_services[1:3]
    print(f"Sliced Services List: {sliced_services}")
    print(f"AWS Services List: {aws_services}")

    list_length=len(aws_services)
    print(f"Number of available AWS Services in this Region: {list_length}")


if __name__ == '__main__':
    main()

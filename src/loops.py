"""Use a list of AWS services and demonstrate various loop operations"""

def main():
    
    aws_services =['S3','Lamda','EC2','DynamoDB','RDS']
    print(f"AWS Services List: {aws_services}")

    # Use a For loop to iterate through the list
    print(f"\nUsing a For loop to iterate through the list of AWS Services:")
    for service in aws_services:
        print(service)

    # Use a While loop to iterate through the list
    print(f"\nUsing a While loop to iterate through the list of AWS Services:")
    index = len(aws_services)-1
    while index >= 0:
        print(aws_services[index])
        index -= 1

    #Using enumarete() with a for loop too get both index and value
    print(f"\nUsing a enumerate() with a for loop to get both index and value of the AWS Services list:")
    for index, service in enumerate(aws_services):
        print(f"Service # {index + 1}: {service}")#added +1 to index so that the numbering starts from 1 rather than 0

if __name__ == '__main__':
    main()
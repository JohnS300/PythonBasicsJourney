"""Create a dictionary of AWS Services and modify the dictionary appropriately"""

def main():
    #Create a dictionary of AWS Services and their descriptions
    aws_services = {
        'S3': "Simple storage service for object storage",
        "Lamda" : "Serverless compute service",
        "EC2": "Elastic compute cloud"
    }
    
    #Print the dictionary
    print(f"Simple dictionary of AWS Services and descriptions :\n{aws_services} ")

    #Access the description of an item in the dictionary
    lambda_description = aws_services['Lamda']
    print(f"\nDescription of Lambda: {lambda_description}")
    
    #Modify the description of a service
    aws_services['Lamda'] = 'AWS Serverless compute service'
    print(f"\nUpdated description of Lambda: {aws_services['Lamda']}")
    
    #Add a new service(key) and its description(value) to the dictionary
    aws_services['SNS'] = 'AWS Simple notification service'
    print(f"\nAdded SNS: {aws_services['SNS']}")

    #Remove the ... Service(key) from the dictionary
    del aws_services['Lamda'] 
    print(f"\nRemoved Lambda from the dictionary: {aws_services}")
    
    
    #Use the keys(), values(), and items() methods to display different aspects of the dictionary
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items())#return the items in the form of a tupol

    
    #Modify the dictionary to add a nested structure with additional information (launch_year)
    aws_services['EC2'] = {
        'description': "Elastic Compute Cloud" ,
        'launch_year': 2006
    }
    print(f"\nModified dictionary with nested structure :\n{aws_services}")
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items())#return the items in the form of a tupol
    

if __name__ == '__main__':
    main()
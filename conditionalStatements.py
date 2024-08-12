"""Determine the appropriete AWS service based on the user's requirments"""
def main():
    # Normally the user_requirment will be a value the input by a user
    user_requirments= 'serverless_computing'
    
    if user_requirments == 'file_storage':
        aws_service='S3'
    elif user_requirments =='virtual_server':
        aws_service='EC2'
    elif user_requirments =='serverless_computing':
        aws_service='Lamda'
    else:
        aws_service='Unknown'
        
    #Print the recomended AWS service based on the user's requirment
    if user_requirments != 'Unknown':
        print(f"The AWS service required is {aws_service}.")
    else:
        print(f"Error: The AWS service is {aws_service}.")

if __name__=='__main__':
    main()
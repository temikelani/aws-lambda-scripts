import boto3 

#create group - use IAC tool for this 
#get all users 
#check which group they belong 
#switch to new group 
REGION = 'us-east-1'

iam = boto3.client('iam', region_name=REGION)
EVALUATE_KEY = 'testing'
EVALUATE_VALUE = 'false'
GROUP_NAME = 'mfa'

def get_all_users():
   return [user.get('UserName') for user in  iam.list_users().get('Users')]

def add_to_groups(user):
  return  iam.add_user_to_group(
    GroupName=GROUP_NAME,
    UserName=user
)

def check_user_tags(user):
    user_ = iam.get_user(UserName=user)
    tags = user_.get('User').get('Tags')
    for tag in tags:
        if tag.get('Key') == EVALUATE_KEY and tag.get('Value') != EVALUATE_VALUE:
            return user
   

def init ():
    # will return ['cohort_user_1', 'cohort_user_2', None, None, None]
    user_list = [user for user in [check_user_tags(u) for u in get_all_users()] if user != None]
    results = [result.get('ResponseMetadata').get('HTTPStatusCode') for result in  [add_to_groups(user) for user in user_list]]

    print(results)

init()
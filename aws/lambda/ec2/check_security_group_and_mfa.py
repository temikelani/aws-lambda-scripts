import boto3 

REGION = 'us-east-1'

#list all sg 
#find all attched sg

#filter 

ec2 = boto3.client('ec2', region_name=REGION)
def get_all_security_groups() -> list:
    return [sg.get('GroupId')for sg in ec2.describe_security_groups().get('SecurityGroups')]

def get_attached_security_groups() -> list:
    base = ec2.describe_instances().get('Reservations')
    return [i.get('Instances')[0]['SecurityGroups'][0].get('GroupId') for i in base]

#lambda 'group' (this is the input for the anon function) : this is the condition  group not in attached_sg_list 
#filter takes an iterable (list) as the second param and evaluates each against lambda condition 
#checks to see if sg from all listings is in attached 
def filter_unattached_sg() -> list:
    return list(filter(lambda group: group not in get_attached_security_groups(), get_all_security_groups()))
  
def delete_unattached_sg(unattached_list):
    for sg in unattached_list:
        try:
            ec2.delete_security_group(GroupId=sg)
        except Exception as e:
            if '"default" cannot be deleted by a user' in str(e):
                print("Unable to delete default security group")

def init():
    delete_unattached_sg(filter_unattached_sg())



if __name__ == "__main__":
    init()


#Elliott Arnold boto3 practice delete sg not attached to EC2 instance  
#5-27-22 
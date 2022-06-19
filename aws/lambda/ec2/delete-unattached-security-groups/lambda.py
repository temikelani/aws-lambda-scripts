import boto3 

region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

#get group ids from list of all security groups

def get_all_security_group_ids() -> list:
  return [sg.get('GroupId')for sg in ec2.describe_security_groups().get('SecurityGroups')]

# get security group ids for all security groups attached to an instance
# keeping in mind an instance could have more that one sg attached

def get_attached_security_group_ids() -> list:
  all_instances = ec2.describe_instances().get('Reservations')
  security_groups = [i.get('Instances')[0]['SecurityGroups'] for i in all_instances]
  return [ i[j].get('GroupId') for i in security_groups for j in range(0, len(i))]


#filter all sg id list for ids not in attached sg id list

def get_unattached_sg_ids() -> list:
  return list(filter(lambda id: id not in get_attached_security_group_ids(), get_all_security_group_ids()))

# delete unattached sgs
def delete_unattached_sg(list_of_unattached_sgs):
  for sg in list_of_unattached_sgs:
    try:
      ec2.delete_security_group(GroupId=sg)
    except Exception as e:
      if '"default" cannot be deleted by a user' in str(e):
        print(f"Unable to delete {sg}, check that it isn't the default sg or referenced by another sg")



def init():
  delete_unattached_sg(get_unattached_sg_ids())


if __name__ == "__main__":
  init()

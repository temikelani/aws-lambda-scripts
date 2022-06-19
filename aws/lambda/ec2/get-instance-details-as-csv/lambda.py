import boto3
import csv
region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)
instance_details = []


for instance in ec2.instances.all():
  result = {}

  result["Instance ID"] = instance.id
  result["Instance State"] = instance.state["Name"]
  result["Launch Time"] = instance.launch_time
  result["Instance Type"] = instance.instance_type
  result["Tags"] = instance.tags

  instance_details.append(result)

print(instance_details)

# field names
fields = [
  "Instance ID",
  "Instance State",
  "Launch Time",
  "Instance Type",
  "Tags"
]

#name of csv file
filename = "reports.csv"

#Writing to csv file
with open(filename,"w") as csvfile:
  # creating a csv dict writer object
  writer = csv.DictWriter(csvfile, fieldnames=fields)

  # writing headeers (field names)
  writer.writeheader()

  #writing data rows
  writer.writerows(instance_details)
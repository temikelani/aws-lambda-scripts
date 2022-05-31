# AWS Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [EC2::User Data Log Location](#1)
- [EC2::Get Instance Metadata ](#2)
- [EC2::Keypair::Filter keypairs by `key-name`](#3)
- [EC2::SecurityGroup::Get Security Group ID](#4)
- [EC2::AMI::Get Latest AMI ID](#5)
- [VPC::Get Default VPC ID](#6)
- [EC2::Get/Query Public IP Address / Filter By Tag / Instance Status](#7)
- [CFN::Cidr Parameter Template ](#8)
- [CFN::Instance Type Parameter Template](#9)
- [CFN::Create a Stack](#10)
- [EC2::Get/Query Public IP Address / Filter By Tag / Instance Status](#11)
- [EC2::Create a KeyPair](#12)
- [EC2::CFN::Block Device Mapping / EBS Volume](#13)
- [CFN::Update a Stack](#14)
- [EC2::Create an Instance](#15)
- [EC2::User data php, get instance id and AZ](#16)
- [EC2::AMI CLI](#17)
- [IAM::ROLE::Assume Role::Trust Relationship](#18)
- [CFN::Create S3 Static Website Bucket](#19)
- [CFN::Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_TemplateQuickRef.html)
- [CFN::Password Param Template](#20)
- [STEP-FX::Example State file](#21)
- [STEP-FX: ALL CChoice Comparsisons](#22)
- [LAMBDA::BOTO3::Code EXamples](#23)
- [CFN::Get Resource ARN](#24)
- [CFN::CFN-FLIP::Convert YAML to JSON](#25)
- [CFN::AWS Parameters Types](#26)
- [CFN::No Echo Property](#27)
- [CLI::--query](#28)
- [CLI::--filter](#29)
- [CFN::User data php, get instance id and AZ ](#30)
- [CLI::Generate-CLI-Skeleton](#31)
- [CLI::Create a tag ](#32)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [go to top](#top)

<br>
<br>
<br>


# EC2::User Data Log Location <a id='1'></a> ([go to top](#top))

- Ec2 User Data Outputs are logged to 

  ```
  var/log/cloud-init-output.log
  ```

- You can reach this dir form inside the instance when you ssh
- Check the logs to ensure smooth operationsof yoru scripts.

<br>
<br>
<br>

# EC2::Get Instance Metadata <a id='2'></a> ([go to top](#top))

```
curl -w "\n" http://169.254.169.254/latest/meta-data/
```
- Complete the url with any of the following to get the metadata specific to that keyword

  ```
  ami-id
  ami-launch-index
  ami-manifest-path
  block-device-mapping/
  events/
  hibernation/
  hostname
  identity-credentials/
  instance-action
  instance-id
  instance-life-cycle
  instance-type
  local-hostname
  local-ipv4
  mac
  metrics/
  network/
  placement/
  profile
  public-hostname
  public-ipv4
  public-keys/
  reservation-id
  security-groups
  services
  ```

- For example

  ```
  curl -w "\n" http://169.254.169.254/latest/meta-data/security-groups
  curl -w "\n" http://169.254.169.254/latest/meta-data/ami-id
  curl -w "\n" http://169.254.169.254/latest/meta-data/hostname
  curl -w "\n" http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
  ```

<br>
<br>
<br>

# EC2::Keypair::Filter keypairs by `key-name`  <a id='3'></a> ([go to top](#top))

```
aws ec2 describe-key-pairs --filters Name=key-name,Values='kp-ue1-test'
```

<br>
<br>
<br>



# EC2::SecurityGroup::Get Security Group ID <a id='4'></a> ([go to top](#top))

```
$sg_name-enter0security-group-name
```
```
SG_ID=$(aws ec2 create-security-group --group-name $sg_name --description "Webserver SG" --vpc-id $vpc_id --output text)
```

<br>
<br>
<br>

# EC2::AMI::Get Latest AMI ID <a id='5'></a> ([go to top](#top))

```
AMI_ID=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1 --query "Parameters[*].[Value]" --output text)
```

```
aws ec2 run-instances \
--image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
--instance-type t2.micro \
--key-name $kp_name \
--security-group-ids $sg_id \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=webserver}]'
```

```
AmiId:
  Description: The latest AMZN Linux 2 AMI 
  Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
  Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
```

<br>
<br>
<br>

# VPC::Get Default VPC ID  <a id='6'></a> ([go to top](#top))

```
VPC_ID=$(aws ec2 describe-vpcs --filters Name=is-default,Values=true --query "Vpcs[*].[VpcId]" --output text)
```

<br>
<br>
<br>

# EC2::Get/Query Public IP Address / Filter By Tag / Instance Status <a id='7'></a> ([go to top](#top))
```
INSTANCE_NAME=webserver
```
```
aws ec2 describe-instances \
--filters "Name=tag:Name,Values=$INSTANCE_NAME" \
--query "Reservations[*].Instances[*].[PublicIpAddress]" \
--output text
```
```
aws ec2 describe-instances \
--filters "Name=tag:Name,Values=$INSTANCE_NAME" "Name=instance-state-name, Values=running" \
--query "Reservations[*].Instances[*].[PublicIpAddress]" \
--output text
```


<br>
<br>
<br>

# CFN::Cidr Parameter Template <a id='8'></a> ([go to top](#top))

```
SshCidr:
  Description: Allow SSH Access from
  Type: String
  MinLength: '9'
  MaxLength: '18'
  Default: '0.0.0.0/0'
  AllowedPattern: (\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})
  ConstraintDescription: must be a valid CIDR range of the form x.x.x.x/x
```

<br>
<br>
<br>



# CFN::Instance Type Parameter Template <a id='9'></a> ([go to top](#top))

```
InstanceType:
  Description: WebServer EC2 instance type
  Type: String
  Default: t2.small
  AllowedValues:
    - t2.micro
    - t2.small
    - t2.medium
```

<br>
<br>
<br>



# CFN::Create a Stack<a id='10'></a> ([go to top](#top))
- [`create-stack`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html)

```
aws cloudformation create-stack \
--stack-name nested-ec2-vpc-iam-ssm-stack \
--template-body file://nested-ec2-vpc-iam-ssm/main.yaml \
--parameters ParameterKey=S3BucketName,ParameterValue=nested-ec2-vpc-iam-ssm ParameterKey=AvailabilityZones,ParameterValue=us-east-1a\\,us-east-1b \
--capabilities CAPABILITY_IAM
```

<br>
<br>
<br>



# EC2::Get/Query Public IP Address / Filter By Tag / Instance Status <a id='11'></a> ([go to top](#top))

```
PUBLIC_DNS=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=$INSTANCE_NAME" "Name=instance-state-name, Values=running" --query "Reservations[*].Instances[*].[PublicDnsName]" --output text)
```
<br>
<br>
<br>


# EC2::Create a KeyPair<a id='12'></a> ([go to top](#top))

```
KP_NAME=kp-ue1-webserver
```
```
aws ec2 create-key-pair --key-name $KP_NAME --key-type rsa --query "KeyMaterial" --output text > secrets/kp-ue1-webserver.pem 
```


<br>
<br>
<br>


# EC2::CFN::Block Device Mapping / EBS Volume <a id='13'></a> ([go to top](#top))

[AWS::EC2::Instance BlockDeviceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-devicename#aws-properties-ec2-blockdev-mapping--examples--Block_device_mapping_with_two_EBS_volumes)
[Amazon EC2 instance root device volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html)

- Depending on the virtualisation type and the AMI, the device name for the root volume is `/dev/xvda` or `/dev/sda1
  - [Device Names](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html#available-ec2-device-names)

- To create an instance with 10GiBs root volume. Edit Block Device Mappings as follows
```
TestInstance:
  Type: AWS::EC2::Instance
  Properties:
    KeyName: !Ref KeyPairName
    ImageId: !Ref AmiId
    InstanceType: !Ref InstanceType
    SecurityGroupIds:
      - !Ref TestSecurityGroup
    BlockDeviceMappings:
      - DeviceName: /dev/xvda
        Ebs:
          VolumeSize: 10
    Tags:
      - Key: Name
        Value: TestInstance
```

- To Create a New Volume

```
TestInstanceVolume:
  Type: AWS::EC2::Volume
  Properties:
    AutoEnableIO: true
    AvailabilityZone: !GetAtt TestInstance.AvailabilityZone
    Size: 10
    Encrypted: true
    Tags:
      - Key: Name
        Value: TestVolume
```

<br>
<br>
<br>


# CFN::Update a Stack <a id='14'></a> ([go to top](#top))

aws cloudformation update-stack \
--stack-name test-stack \
--template-body file://cfn-template.yaml 


<br>
<br>
<br>


# EC2::Create an Instance <a id='15'></a> ([go to top](#top))
```
KP_NAME=kp-ue1-webserver
aws ec2 create-key-pair --key-name $KP_NAME --key-type rsa --query "KeyMaterial" --output text > secrets/kp-ue1-webserver.pem 

SG_NAME=webserver-sg-ue1
VPC_ID=$(aws ec2 describe-vpcs --filters Name=is-default,Values=true --query "Vpcs[*].[VpcId]" --output text)
SG_ID=$(aws ec2 create-security-group --group-name $SG_NAME --description "Webserver SG" --vpc-id $VPC_ID --output text)

AMI_ID=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1 --query "Parameters[*].[Value]" --output text)

aws ec2 authorize-security-group-ingress \
--group-id $SG_ID \
--protocol tcp \
--port 22 \
--cidr 0.0.0.0/0
```

- EC2 with latest AMI, custom SG, tags, default subnet and user data
```
aws ec2 run-instances \
--image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
--instance-type t2.micro \
--key-name $KP_NAME \
--security-group-ids $SG_ID \
--user-data file://userdata.txt \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=webserver}]'
```

- EC2 with custom AMI, SG, userdata, tag and default subnet
```
aws ec2 run-instances \
--image-id $AMI_ID \
--instance-type t2.micro \
--key-name $KP_NAME \
--security-group-ids $SG_ID \
--user-data file://userdata.txt \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=webserver}]'
```

- EC2 with latest AMI, custom SG, tags, default subnet and user data and 10GiBs root storage
  - [Block Device Mappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html)

```
aws ec2 run-instances \
--image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
--block-device-mappings file://mapping.json \
--instance-type t2.micro \
--key-name $KP_NAME \
--security-group-ids $SG_ID \
--user-data file://userdata.txt \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=webserver}]'
```

- mapping.json

```json
[
  {
    "DeviceName": "/dev/xvda",
    "Ebs" : {
      "VolumeSize":10
    }
  }
]
```

<br>
<br>
<br>

# EC2::User data php, get instance id and AZ <a id='16'></a> ([go to top](#top))

```
 UserData:
        !Base64 |
          #!/bin/bash
          yum update -y
          yum install -y httpd php
          systemctl start httpd
          systemctl enable httpd
          usermod -a -G apache ec2-user
          chown -R ec2-user:apache /var/www
          chmod 2775 /var/www
          find /var/www -type d -exec chmod 2775 {} \;
          find /var/www -type f -exec chmod 0664 {} \;
          # PHP script to display Instance ID and Availability Zone
          cat << 'EOF' > /var/www/html/index.php
            <!DOCTYPE html>
            <html>
            <body>
              <center>
                <?php
                # Get the instance ID from meta-data and store it in the $instance_id variable
                $url = "http://169.254.169.254/latest/meta-data/instance-id";
                $instance_id = file_get_contents($url);
                # Get the instance's availability zone from metadata and store it in the $zone variable
                $url = "http://169.254.169.254/latest/meta-data/placement/availability-zone";
                $zone = file_get_contents($url);
                ?>
                <h2>EC2 Instance ID: <?php echo $instance_id ?></h2>
                <h2>Availability Zone: <?php echo $zone ?></h2>
              </center>
            </body>
            </html>
          EOF
```

<br>

- Describe an AMI

  ```
  aws ec2 describe-images \
  --region enter-region-here \
  --image-ids enter-ami-id-here
  ```

- Describe AMIs by owner and return only the AMI ID

  ```
  aws ec2 describe-images \
  --owners enter-your-account-id-here \
  --query 'Images[*].[ImageId]'
  ```

- Describe AMIs, filter by tag, return only the AMI ID

  ```
  aws ec2 describe-images \
  --filters "Name=tag:Name,Values=enter-value-of-tag-name" \
  --query 'Images[*].[ImageId]' \
  --output text
  ```

- Describe AMIs owned by amazon, filter by root device type

  ```
  aws ec2 describe-images --owners self amazon \
  --filters "Name=root-device-type,Values=ebs" \
  --query 'Images[*].[ImageId]'
  ```

- List all public AMIs, including any public AMIs that you own.

  ```
  aws ec2 describe-images --executable-users all
  ```

- List the AMIs for which you have `explicit launch permissions`. This list does not include any AMIs that you own.
  ```
  aws ec2 describe-images --executable-users self
  ```

<br>
<br>
<br>

# IAM::ROLE::Assume Role::Trust Relationship <a id='18'></a> ([go to top](#top))

- To allow a service assume a role you must edit the role's trust relationship document
- This allows a service/user assume that role and all its permissions.
- The block below allows the following to assume a role
  - config
  - cloudformation
  - and a dummy account that you own with ID `123456789123`
  - and a dummy external account that with ID `123456789123`, required external ID `sampleExternalID` and MFA requirement
  
  <br>

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                  "Service": "cloudformation.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
          },
          {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                  "Service": "config.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
          },
          {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": "123456789123"
            },
            "Condition": {}
          },
          {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": "123456789123"
            },
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "sampleExternalID"
                },
                "Bool": {
                    "aws:MultiFactorAuthPresent": true
                }
            }
          }
      ]
  }
  ```

<br>
<br>
<br>


# CFN::Create S3 Static Website Bucket <a id='19'></a> ([go to top](#top))

```
Parameters:
  s3BucketName:
    Description: the bucketname for this site
    Type: String
    Default: randomsite-gshfgshf7.com

Resources:
  s3Bucket:
    Type: AWS::S3::Bucket
    Properties: 
      AccessControl: PublicRead 
      BucketName: !Ref s3BucketName
      # CorsConfiguration: 
      # LifecycleConfiguration: 
      # NotificationConfiguration: 
      # VersioningConfiguration: 
      WebsiteConfiguration: 
        IndexDocument: index.html
        ErrorDocument: error.html
      Tags:
        - Key: Purpose
          Value: Holds My Website

Outputs:
  WebsiteURL:
    Value: !GetAtt s3Bucket.WebsiteURL
    Description: URL for website hosted on S3
  S3BucketSecureURL: 
    Value: !Sub "https://${s3Bucket.DomainName}"
    Description: Name of S3 bucket to hold website content
```
<br>
<br>
<br>


# CFN::Password Param Template <a id='20'></a> ([go to top](#top))

```
password:
  NoEcho: 'true'
  Description: 
  Type: String
  Default: y!User1Login8P@ssword
  MinLength: '1'
  MaxLength: '41'
  AllowedPattern: '[a-zA-Z0-9]*'
  ConstraintDescription: must contain only alphanumeric characters.
```

<br>
<br>
<br>


# STEP-FX::Example State File <a id='21'></a> ([go to top](#top))

```
{
	"Comment": "An example of the Amazon States Language using a Parallel and a Choice state to execute two branches at the same time.",
	"StartAt": "StartTask",
	"States": {
		"StartTask": {
			"Type": "Parallel",
			"Next": "CWMetric",
			"Branches": [
      {
        "StartAt": "Gen Report",
        "States": {
          "Gen Report": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-west-2:ACCOUNT_ID:function:GenerateReport",
            "End": true
          }
        }
			}, 
      {
        "StartAt": "UpdateDB",
        "States": {
          "UpdateDB": {
            "Type": "Choice",
            "Choices": [{
              "Variable": "$.level",
              "StringEquals": "latest",
              "Next": "Last Level"
            }],
            "Default": "Simple Level"
          },
          "Last Level": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-west-2:ACCOUNT_ID:function:EndsLastLevel",
            "End": true
          },
          "Simple Level": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-west-2:ACCOUNT_ID:function:EndsSimpleLevel",
            "End": true
          }
        }
			}
      ]
		},
		"CWMetric": {
			"Type": "Task",
			"Resource": "arn:aws:lambda:us-west-2:ACCOUNT_ID:function:PutMetric",
			"End": true
		}
	}
}
```

```
Comment: An example of the Amazon States Language using a Parallel and a Choice state to execute two branches at the same time.
StartAt: StartTask
States:
  StartTask:
    Type: Parallel
    Next: CWMetric
    Branches:
      - StartAt: GenReport
        States:
          GenReport:
            Type: Task
            Resource: arn:aws:lambda:us-west-2:ACCOUNT_ID:function:GenerateReport
            End: true
      - StartAt: UpdateDB
        States:
          UpdateDB:
            Type: Choice
            Choices:
              - Variable: $.level
                StringEquals: latest
                Next: Last Level
            Default: Simple Level
          Last Level:
            Type: Task
            Resource: arn:aws:lambda:us-west-2:ACCOUNT_ID:function:EndsLastLevel
            End: true
          Simple Level:
            Type: Task
            Resource: arn:aws:lambda:us-west-2:ACCOUNT_ID:function:EndsSimpleLevel
            End: true
  CWMetric:
    Type: Task
    Resource: arn:aws:lambda:us-west-2:ACCOUNT_ID:function:PutMetric
    End: true
```

<br>
<br>
<br>

# STEP-FX: ALL CChoice Comparsisons <a id='22'></a> ([go to top](#top))

```yaml
String comparisons:
  StringEquals
  StringLessThan
  StringGreaterThan
  StringLessThanEquals
  StringGreaterThanEquals

Number comparisons:
  NumericEquals
  NumericLessThan
  NumericGreaterThan
  NumericLessThanEquals
  NumericGreaterThanEquals
  Boolean comparisons: BooleanEquals.

# And arguably the most powerful
Timestamp conditions:
  TimestampEquals
  TimestampLessThan
  TimestampGreaterThan
  TimestampLessThanEquals
  TimestampGreaterThanEquals
```

<br>
<br>
<br>

# LAMBDA::BOTO3:: Code Examples <a id='23'></a> ([go to top](#top))

[All Examles](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/examples.html)

[DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)

<br>
<br>
<br>

# CFN::Get Resource ARN <a id='24'></a> ([go to top](#top))

```
Resource: !Sub 'arn:${AWS::Partition}:ssm:${AWS::Region}:${AWS::AccountId}:parameter/${BasicParameter}'
```

<br>
<br>
<br>

# CFN::Convert YAML to JSON <a id='25'></a> ([go to top](#top))


[Flipping formats](https://cfn101.workshop.aws/basics/templates/flipping-formats-and-cleanup.html)

<hr>
<br>

- run either command to install `cfn-flip`

```
pip install cfn-flip
cfn-flip --version
```
```
brew install cfn-flip
cfn-flip --version
```

<br>

- input to output

```
cfn-flip json-file.json enter-yaml-file-name.yaml
```
```
cfn-flip yaml-file.yaml enter-json-file-name.json 
```

<br>

- to yaml `-y` option
- to json use `-j` option

  ```
  cfn-flip json-file.json -y
  ```
  ```
  cfn-flip yaml-file.json -j
  ```

<br>

- help

  ```
  cfn-flip --help
  ```

<br>
<br>
<br>

# CFN::AWS Parameters Types <a id='26'></a> ([go to top](#top))

- [AWS-specific parameter types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-specific-parameter-types)

- [SSM parameter types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types)

<hr>
<br>

```
Parameters:
  KeyPair: 
    Description: Amazon EC2 Key Pair
    Type: AWS::EC2::KeyPair::KeyName

  VpcId:
    Description: Enter the VpcId
    Type: AWS::EC2::VPC::Id

  SubnetIds:
    Description: Enter the Subnets
    Type: List<AWS::EC2::Subnet::Id>

  SubnetId:
    Description: Enter the Subnets
    Type: AWS::EC2::Subnet::Id

  AvailabilityZone:
    Type: AWS::EC2::AvailabilityZone::Name

  AvailabilityZones:
    Description: An array of Availability Zones for a region, such as us-west-2a, us-west-2b.
    Type: List<AWS::EC2::AvailabilityZone::Name>

  AmiID:
    Description: The ID of the AMI.
    Type: AWS::EC2::Image::Id

  AmiIDs:
    Description: An array of Amazon EC2 image IDs, such as ami-0ff8a91507f77f867, ami-0a584ac55a7631c0c. Note that the AWS CloudFormation console doesn't show a drop-down list of values for this parameter type.
    Type: AWS::EC2::Image::Id

  InstanceTypeParameter:
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - m1.small
      - m1.large
    Description: Enter t2.micro, m1.small, or m1.large. Default is t2.micro.

```

<br>
<br>
<br>

# CFN::No Echo Property <a id='27'></a> ([go to top](#top))

```
Parameters
  DBPassword:
    NoEcho: 'true'
    Description: Password for MySQL database access
    Type: String
    MinLength: '1'
    MaxLength: '41'
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
```

<br>
<br>
<br>

# CLI::--query <a id='28'></a> ([go to top](#top))

- run

```
aws ec2 describe-key-pairs
```

- and you get the response

```
{
    "KeyPairs": [
        {
            "KeyPairId": "key-0cb81e98f197b5a84",
            "KeyFingerprint": "69:33:c1:b0:0c:12:16:13:49:68:96:41:1a:03:20:79:23:ea:d5:d3",
            "KeyName": "kp-ue1-test",
            "KeyType": "rsa",
            "Tags": []
        },
        {
            "KeyPairId": "key-047ebcfb49a3a3bb5",
            "KeyFingerprint": "Ua6X8IvRy9oLRk9ntaaKyIGm8oPwiezhi/EsCH6wJbU=",
            "KeyName": "kp-ue1-3rdparty",
            "KeyType": "ed25519",
            "Tags": []
        }
    ]
}
```

- to query by any on the responses use

```
aws ec2 describe-key-pairs --query 'KeyPairs[*].[KeyPairId]'
```

- the response is

```
[
  [
      "key-0cb81e98f197b5a84"
  ],
  [
      "key-047ebcfb49a3a3bb5"
  ]
]
```

<br>
<br>
<br>

# CLI::--filter <a id='29'></a> ([go to top](#top))


```
  aws ec2 describe-key-pairs --filters Name=key-name,Values='kp-ue1-test'
```

<br>
<br>
<br>

# CFN::User data php, get instance id and AZ <a id='30'></a> ([go to top](#top))

check for mareks code too

```
 UserData:
        !Base64 |
          #!/bin/bash
          yum update -y
          yum install -y httpd php
          systemctl start httpd
          systemctl enable httpd
          usermod -a -G apache ec2-user
          chown -R ec2-user:apache /var/www
          chmod 2775 /var/www
          find /var/www -type d -exec chmod 2775 {} \;
          find /var/www -type f -exec chmod 0664 {} \;
          # PHP script to display Instance ID and Availability Zone
          cat << 'EOF' > /var/www/html/index.php
            <!DOCTYPE html>
            <html>
            <body>
              <center>
                <?php
                # Get the instance ID from meta-data and store it in the $instance_id variable
                $url = "http://169.254.169.254/latest/meta-data/instance-id";
                $instance_id = file_get_contents($url);
                # Get the instance's availability zone from metadata and store it in the $zone variable
                $url = "http://169.254.169.254/latest/meta-data/placement/availability-zone";
                $zone = file_get_contents($url);
                ?>
                <h2>EC2 Instance ID: <?php echo $instance_id ?></h2>
                <h2>Availability Zone: <?php echo $zone ?></h2>
              </center>
            </body>
            </html>
          EOF
```

<br>
<br>
<br>

# CLI::CLI Generate Skeleton <a id='31'></a> ([go to top](#top))

- see what that aws command requires/supports?

```
aws ec2 create-vpc --generate-cli-skeleton
```

<br>
<br>
<br>

# CLI::Create a tag <a id='32'></a> ([go to top](#top))

```
aws ec2 create-tags --resources vpc-30783443 --tags Key=Network,Value=Default
```

<br>
<br>
<br>

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))


<br>
<br>
<br>


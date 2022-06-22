# EC2 CLI Notes <a id ='top'></a>

<br>
<br>

# Contents

- [AMI: `describe-images`](#1)
- [AMI: SSM Latest Amazon Lnux AMI](#2)
- [AMI / INSTANCE: Locate authorized keys](#3)
- [](#4)
- [](#5)
- [](#6)
- [](#7)
- [](#8)
- [](#9)
- [](#10)
- [](#11)
- [](#12)
- [](#13)
- [](#14)
- [](#15)
- [](#16)
- [](#17)
- [](#18)
- [](#19)
- [](#20)
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

# AMI: `describe-images` <a id='1'></a> ([go to top](#top))

- [Documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html)
- `Omitting the --owners flag` from the describe-images command` returns all images for which you have launch permissions, regardless of ownership.`

```bash
aws ec2  describe-images
--executable-users <value>  \
--filters <value> \
--image-ids <value> \
--owners <value> \
--include-deprecated | --no-include-deprecated \
--dry-run | --no-dry-run \
--cli-input-json | --cli-input-yaml \
--generate-cli-skeleton <value> \
--query
```

- Examples

```bash
aws ec2  describe-images
--executable-users all | self \
--filters "Name=platform,Values=windows" "Name=root-device-type,Values=ebs" "Name=tag:Type,Values=Custom"\
--image-ids ami-065efef2c739d613b \
--owners self amazon 123456789012 \
--query 'Images[*].[ImageId]' \
--output json
```

- Output

```json
{
  "Images": [
    {
      "Architecture": "x86_64",
      "CreationDate": "2022-06-14T19:44:18.000Z",
      "ImageId": "ami-065efef2c739d613b",
      "ImageLocation": "amazon/amzn2-ami-hvm-2.0.20220606.1-x86_64-gp2",
      "ImageType": "machine",
      "Public": true,
      "OwnerId": "137112412989",
      "PlatformDetails": "Linux/UNIX",
      "UsageOperation": "RunInstances",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0c87771c8e09de699",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Amazon Linux 2 AMI 2.0.20220606.1 x86_64 HVM gp2",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "ImageOwnerAlias": "amazon",
      "Name": "amzn2-ami-hvm-2.0.20220606.1-x86_64-gp2",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm",
      "DeprecationTime": "2024-06-14T19:44:18.000Z"
    }
  ]
}
```

```yaml
Images:
  - Architecture: x86_64
    BlockDeviceMappings:
      - DeviceName: /dev/xvda
        Ebs:
          DeleteOnTermination: true
          Encrypted: false
          SnapshotId: snap-0c87771c8e09de699
          VolumeSize: 8
          VolumeType: gp2
    CreationDate: "2022-06-14T19:44:18.000Z"
    DeprecationTime: "2024-06-14T19:44:18.000Z"
    Description: Amazon Linux 2 AMI 2.0.20220606.1 x86_64 HVM gp2
    EnaSupport: true
    Hypervisor: xen
    ImageId: ami-065efef2c739d613b
    ImageLocation: amazon/amzn2-ami-hvm-2.0.20220606.1-x86_64-gp2
    ImageOwnerAlias: amazon
    ImageType: machine
    Name: amzn2-ami-hvm-2.0.20220606.1-x86_64-gp2
    OwnerId: "137112412989"
    PlatformDetails: Linux/UNIX
    Public: true
    RootDeviceName: /dev/xvda
    RootDeviceType: ebs
    SriovNetSupport: simple
    State: available
    UsageOperation: RunInstances
    VirtualizationType: hvm
```

<br>
<br>
<br>

# AMI: SSM Latest Amazon Lnux AMI <a id='2'></a> ([go to top](#top))

- [Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html#finding-an-ami-parameter-store)

```bash
aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1 --query "Parameters[*].[Value]" --output text
```

```bash
AMI_ID=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1 --query "Parameters[*].[Value]" --output text)
```

```bash
aws ec2 run-instances \
--image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
--instance-type t2.micro \
--key-name $KP_NAME \
--security-group-ids $SG_ID \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=webserver}]'
```

```yaml
AmiId:
  Description: The latest AMZN Linux 2 AMI
  Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
  Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
```

<br>
<br>
<br>

# AMI / INSTANCE: Locate authorized keys <a id='3'></a> ([go to top](#top))

- [Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/usingsharedamis-finding.html#usingsharedamis-confirm)

- `cd home/ec2-user`

```
sudo find / -name "authorized_keys" -print -exec cat {} \;
```

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

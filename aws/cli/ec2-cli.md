# EC2 CLI Notes <a id ='top'></a>

<br>
<br>

# Contents

- [AMI: `describe-images`](#1)
- [AMI: SSM Latest Amazon Lnux AMI](#2)
- [AMI / INSTANCE: Locate authorized keys](#3)
- [AMI: `modify-image-attribute`: Make image public](#4)
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

- [CLI Docs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html)
- `Omitting the --owners flag` from the describe-images command` returns all images for which you have launch permissions, regardless of ownership.`

```bash
aws ec2  describe-images
--executable-users all | self \
--filters "Name=platform,Values=windows" "Name=root-device-type,Values=ebs" "Name=tag:Type,Values=Custom" \
--image-ids ami-065efef2c739d613b \
--owners self amazon 123456789012 \
--query 'Images[*].[ImageId]' \
--output json
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

```bash
sudo find / -name "authorized_keys" -print -exec cat {} \;
```

<br>
<br>
<br>

# AMI: `modify-image-attribute`: Make image public/private <a id='4'></a> ([go to top](#top))

- [Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-intro.html#sharingamis-cli)
- [CLI Docs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html)

```bash
aws ec2 modify-image-attribute \
--image-id ami-0abcdef1234567890 \
--launch-permission "Add=[{Group=all}]"
```

```bash
aws ec2 modify-image-attribute \
--image-id ami-0abcdef1234567890 \
--launch-permission "Remove=[{Group=all}]"
```

```bash
aws ec2 modify-image-attribute \
    --image-id ami-5731123e \
    --launch-permission "Add=[{UserId=123456789012}]"
```

```
aws ec2 modify-image-attribute \
    --image-id ami-5731123e \
    --launch-permission "Remove=[{UserId=123456789012}]"
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

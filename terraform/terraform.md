# Terraform Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [Resources](#0)
- [`terraform init`](#1)
- [`terraform plan`](#2)
- [`terraform apply`](#3)
- [`terraform destroy`](#4)
- [`terraform state`](#5)
- [`terraform workspace`](#6)
- [`terraforn import`](#7)
- [Setup Credentials](#8)
- [`terraform validate `](#9)
- [aws required provider](#10)
- [aws multiple providers (multi-region)](#11)
- [`terraform show`](#12)
- [`terraform console`](#13)
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
- [console, format, output, expressions, provisioner, lookup, length, cidr functions, locals, ariable types, type-object, cudr subnet](#)
- [go to top](#top)

<br>
<br>
<br>

# Resources <a id='0'></a> ([go to top](#top))

- [Terraform Commands](https://www.terraform.io/cli/commands)

<br>
<br>
<br>

# `terraform init` <a id='1'></a> ([go to top](#top))

[Documentation](https://www.terraform.io/cli/commands/init)

```
terraform init
```

<br>
<br>
<br>

# `terraform plan` <a id='2'></a> ([go to top](#top))

[Documentation](https://www.terraform.io/cli/commands/plan)

```
Usage: terraform plan [options]
```

```
terraform plan
```

```
terraform plan -out [plan-name]
terraform plan -out=[FILENAME]
```

<br>
<br>
<br>

# `terraform apply` <a id='3'></a> ([go to top](#top))

[Documentation](https://www.terraform.io/cli/commands/apply)

```
Usage: terraform apply [options] [plan file]
```

```
terraform apply
terraform apply -auto-approve
```

```
terraform apply -var-file='="./dev.tfvars"
terraform apply -var-file='="./prod.tfvars"
```

<br>
<br>
<br>

# `terraform destroy` <a id='4'></a> ([go to top](#top))

[Documentation](https://www.terraform.io/cli/commands/destroy)

```
Usage: terraform destroy [options]
```

```
terraform destroy -auto-approve
```

<br>
<br>
<br>

# `terraform state` <a id='5'></a> ([go to top](#top))

- [Documentation](https://www.terraform.io/cli/commands/state/list)
- [Documentation](https://www.terraform.io/cli/commands/state/show)
- [Documentation](https://www.terraform.io/cli/commands/state/mv)
- [Documentation](https://www.terraform.io/cli/commands/state/rm)

```
Usage: terraform state list [options] [address...]
Usage: terraform state show [options] ADDRESS
Usage: terraform state mv [options] SOURCE DESTINATION
Usage: terraform state rm [options] ADDRESS...
```

```
terraform state list
terraform state list -state=path-to-state-file
terraform state list aws_instance.bar
terraform state list module.elb
terraform state list -id=sg-1234abcd
```

```
terraform state show 'packet_device.worker'
terraform state show 'module.foo.packet_device.worker'
terraform state show 'packet_device.worker[0]'
```

```
terraform state mv -state-out=../project-1/terraform.tfstate aws_vpc.main aws_vpc.my_vpc

# rename a resource
terraform state mv packet_device.worker packet_device.helper

# move resource into a module
terraform state mv packet_device.worker module.worker.packet_device.worker
terraform state mv packet_device.worker module.worker.packet_device.main
```

<br>
<br>
<br>

# `terraform workspace` <a id='6'></a> ([go to top](#top))

- [Documentation](https://www.terraform.io/cli/commands/workspace/list)
- [Documentation](https://www.terraform.io/cli/commands/workspace/select)
- [Documentation](https://www.terraform.io/cli/commands/workspace/new)
- [Documentation](https://www.terraform.io/cli/commands/workspace/delete)
- [Documentation](https://www.terraform.io/cli/commands/workspace/show)

```
Usage: terraform workspace list [DIR]
Usage: terraform workspace select NAME [DIR]
Usage: terraform workspace new [OPTIONS] NAME [DIR]
```

```
terraform workspace --help
terraform workspace list
```

```
terraform workspace new dev
terraform workspace new -state=old.terraform.tfstate example
```

```
terraform workspace select dev
terraform workspace select default
```

```
terraform workspace delete dev # delete dev workspace
```

```
resource "aws_sqs_queue" "queue" {
    name = "${terraform.workspace}-queue"
}
```

<br>
<br>
<br>

# `terraform import` <a id='7'></a> ([go to top](#top))

[Documentation](https://www.terraform.io/cli/commands/import)

```
Usage: terraform import [options] ADDRESS ID
```

- Obtain the ID of the resource you want to import
- `terraform import <resource_type>.<resource_identifier> <value>`

```
terraform import aws_vpc.dev vpc-0ce9e2544b6d49d97
```

- OR

```
VpcID=$(aws ec2 describe-vpcs --region us-west-2 --filters Name=tag:Name,Values='Web VPC' --output text --query "Vpcs[].VpcId")
terraform import aws_vpc.dev $VpcID
```

- Run `terraform show` to get resource details for `aws_vpc.dev`

```
terraform show
```

- Copy the aadinable properties into your terraform file

```terraform
resource "aws_vpc" "dev" {
    assign_generated_ipv6_cidr_block = false
    cidr_block                       = "192.168.100.0/24"
    enable_classiclink               = false
    enable_classiclink_dns_support   = false
    enable_dns_hostnames             = true
    enable_dns_support               = true
    instance_tenancy                 = "default"
    tags                             = {
        "Name"                        = "Web VPC"
        "ca-creator"                  = "system"
        "ca-environment"              = "production"
        "ca-environment-session-id"   = "1282472"
        "ca-environment-session-uuid" = "5e814446-6e90-46f8-81bd-cd7562e2328f"
        "ca-persistent"               = "false"
        "ca-scope"                    = "lab"
    }
}
```

<br>
<br>
<br>

# Setup Credentials <a id='8'></a> ([go to top](#top))

- [Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration)

- Terraform will puse default cret=dentials set when you run

```
aws configure
```

- Or you can set the credentials as env vars

```
provider "aws" {}
```

```
export AWS_ACCESS_KEY_ID=shjakvbslavbdsvbd
export AWS_SECRET_ACCESS_KEY=hsjalbfhvsalvfsavfuasobv
export AWS_REGION="us-west-2"
terraform plan
```

```
export AWS_PROFILE
AWS_CONFIG_FILE
```

- Or you can supply tf the path for a specific set of credentials

```
provider "aws" {
  shared_config_files      = ["~/.aws/conf"]
  shared_credentials_files = ["~/.aws/creds"]
  profile                  = "terraform"
}
```

- Or `terraform` can Assume a Role

```
provider "aws" {
  assume_role {
    role_arn     = "arn:aws:iam::123456789012:role/ROLE_NAME"
    session_name = "SESSION_NAME"
    external_id  = "EXTERNAL_ID"
  }
}
```

<br>
<br>
<br>

# `terraform validate` <a id='9'></a> ([go to top](#top))

- [Documentation](https://www.terraform.io/cli/commands/validate)
- Validate runs checks that verify whether a configuration is syntactically valid and internally consistent, regardless of any provided variables or existing state

```
Usage: terraform validate [options]
```

<br>
<br>
<br>

# aws required provider <a id='10'></a> ([go to top](#top))

[Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

```
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.18.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}
```

<br>
<br>
<br>

# aws multiple providers (multi-region) <a id='11'></a> ([go to top](#top))

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.12"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}

provider "aws" {
    region = "us-east-2"
    alias = "ohio"
}

resource "aws_vpc" "n_virginia_vpc" {
    cidr_block = "10.0.0.0/16"
}

resource "aws_vpc" "ohio_vpc" {
    cidr_block = "10.1.0.0/16"
    provider = "aws.ohio"
}
```

<br>
<br>
<br>

# `terraform show` <a id='12'></a> ([go to top](#top))

- [Documentation](https://www.terraform.io/cli/commands/show/)
- `provide human-readable output from a state or plan file.`

```
Usage: terraform show [options] [file]
```

<br>
<br>
<br>

# `terraform console`<a id='13'></a> ([go to top](#top))

- [Documentation](https://www.terraform.io/cli/commands/console)
- provides an interactive command-line console for evaluating and experimenting with expressions.

```
Usage: terraform console [options]
```

```terraforom
variable "apps" {
  type = map(any)
  default = {
    "foo" = {
      "region" = "us-east-1",
    },
    "bar" = {
      "region" = "eu-west-1",
    },
    "baz" = {
      "region" = "ap-south-1",
    },
  }
}

resource "random_pet" "example" {
  for_each = var.apps
}
```

```bash
terraform console
```

```terraform
> var.apps.foo
{
  "region" = "us-east-1"
}

> cidrnetmask("172.16.0.0/12")
"255.240.0.0"
```

<br>
<br>
<br>

# variables <a id='14'></a> ([go to top](#top))

- [Documentation](https://www.terraform.io/language/values)

- syntax

```terraform
variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server."

  validation {
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
}
```

- Use a specific `tfvars file`

```
terraform apply -var-file="testing.tfvars"
```

<br>

## variables: string <a id='14a'></a> ([go to top](#top))

```
variable "image_id" {
  type = string
}

variable "instance_type" {
    description = "Size of the EC2 instance"
    type = string
}
```

```
resource "aws_instance" "server" {
  ami = var.image_id
  instance_type = var.instance_type
}
```

- `terraform.tfvars file`

```
instance_type      = "t3.micro"
image_id           = "ami-42895639563865395"
```

<br>

## variables: list(string) <a id='14b'></a> ([go to top](#top))

```
variable "availability_zones" {
  type = list(string)
}
```
```
resource "aws_subnet" "subnet1" {
  availability_zone = var.availability_zones[0]
}
resource "aws_subnet" "subnet2" {
  availability_zone = var.availability_zones[1]
}
```
- `terraform.tfvars` file
```
availability_zones = ["us-east-1a", "us-east-1b"]
cidr_block         = "10.0.0.0/16"
instance_type      = "t3.micro"
key_name           = "cloudacademydemo"
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

```

```

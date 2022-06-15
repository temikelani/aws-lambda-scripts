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
- [variables](#14)
  - [variables: `string`](#14a)
  - [variables: `object`](#14b)
  - [variables: `map`](#14c)
  - [variables: `number`](#14d)
  - [variables: `list(string)`](#14e)
  - [variables: `list(map`](#14f)
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
- [console, format, output, expressions, provisioner, lookup, length, cidr functions, locals, ariable types, type-object, cudr subnet, conditional ? 1:0, count, type: bool](#)
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

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/init)

```bash
terraform init
```

</details>

<br>
<br>
<br>

# `terraform plan` <a id='2'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/plan)

```
Usage: terraform plan [options]
```

```bash
terraform plan
```

```bash
terraform plan -out [plan-name]
terraform plan -out=[FILENAME]
```

</details>

<br>
<br>
<br>

# `terraform apply` <a id='3'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/apply)

```
Usage: terraform apply [options] [plan file]
```

```bash
terraform apply
terraform apply -auto-approve
```

```bash
terraform apply -var-file="./dev.tfvars"
terraform apply -var-file="./prod.tfvars"
```

</details>

<br>
<br>
<br>

# `terraform destroy` <a id='4'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/destroy)

```
Usage: terraform destroy [options]
```

```bash
terraform destroy
terraform destroy -auto-approve
```

</details>

<br>
<br>
<br>

# `terraform state` <a id='5'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

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

```bash
terraform state list
terraform state list -state=path-to-state-file
terraform state list aws_instance.bar
terraform state list module.elb
terraform state list -id=sg-1234abcd
```

```bash
terraform state show 'packet_device.worker'
terraform state show 'module.foo.packet_device.worker'
terraform state show 'packet_device.worker[0]'
```

```bash
terraform state mv -state-out=../project-1/terraform.tfstate aws_vpc.main aws_vpc.my_vpc

# rename a resource
terraform state mv packet_device.worker packet_device.helper

# move resource into a module
terraform state mv packet_device.worker module.worker.packet_device.worker
terraform state mv packet_device.worker module.worker.packet_device.main
```

</details>

<br>
<br>
<br>

# `terraform workspace` <a id='6'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

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

```bash
terraform workspace --help
terraform workspace list
```

```bash
terraform workspace new dev
terraform workspace new -state=old.terraform.tfstate example
```

```bash
terraform workspace select dev
terraform workspace select default
```

```bash
terraform workspace delete dev # delete dev workspace
```

```terraform
resource "aws_sqs_queue" "queue" {
    name = "${terraform.workspace}-queue"
}
```

</details>

<br>
<br>
<br>

# `terraform import` <a id='7'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/import)

```bash
Usage: terraform import [options] ADDRESS ID
```

- Obtain the ID of the resource you want to import
- `terraform import <resource_type>.<resource_identifier> <value>`

```bash
terraform import aws_vpc.dev vpc-0ce9e2544b6d49d97
```

- OR

```bash
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

</details>

<br>
<br>
<br>

# Setup Credentials <a id='8'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration)
- Terraform will use default credentials set when you run

```bash
aws configure
```

- Or you can set the credentials as env vars

```terraform
provider "aws" {}
```

```bash
export AWS_ACCESS_KEY_ID=shjakvbslavbdsvbd
export AWS_SECRET_ACCESS_KEY=hsjalbfhvsalvfsavfuasobv
export AWS_REGION="us-west-2"
terraform plan
```

```bash
export AWS_PROFILE
export AWS_CONFIG_FILE
```

- Or you can supply tf the path for a specific set of credentials

```terraform
provider "aws" {
  shared_config_files      = ["~/.aws/conf"]
  shared_credentials_files = ["~/.aws/creds"]
  profile                  = "terraform"
}
```

- Or `terraform` can Assume a Role

```terraform
provider "aws" {
  assume_role {
    role_arn     = "arn:aws:iam::123456789012:role/ROLE_NAME"
    session_name = "SESSION_NAME"
    external_id  = "EXTERNAL_ID"
  }
}
```

</details>

<br>
<br>
<br>

# `terraform validate` <a id='9'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/validate)
- Validate runs checks that verify whether a configuration is syntactically valid and internally consistent, regardless of any provided variables or existing state

```
Usage: terraform validate [options]
```

</details>

<br>
<br>
<br>

# aws required provider <a id='10'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

```terraform
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

</details>

<br>
<br>
<br>

# aws multiple providers (multi-region) <a id='11'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
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

</details>

<br>
<br>
<br>

# `terraform show` <a id='12'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/show/)
- `provide human-readable output from a state or plan file.`

```
Usage: terraform show [options] [file]
```

</details>

<br>
<br>
<br>

# `terraform console`<a id='13'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

- [Documentation](https://www.terraform.io/cli/commands/console)
- provides an interactive command-line console for evaluating and experimenting with expressions.

```
Usage: terraform console [options]
```

```terraform
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

</details>

<br>
<br>
<br>

# variables <a id='14'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

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

```terraform
terraform apply -var-file="testing.tfvars"
```

</details>

<br>

## variables: string <a id='14a'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
variable "image_id" {
  type = string
}

variable "instance_type" {
    description = "Size of the EC2 instance"
    type = string
}
```

```terraform
resource "aws_instance" "server" {
  ami = var.image_id
  instance_type = var.instance_type
}
```

- `terraform.tfvars file`

```terraform
instance_type      = "t3.micro"
image_id           = "ami-42895639563865395"
```

</details>

<br>

## variables: object <a id='14b'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
variable "disk" {
  description = "OS image to deploy"
  type = object({
    delete_on_termination = bool
    encrypted = bool
    volume_size = string
    volume_type = string
  })
}

variable "docker_ports" {
  type = list(object({
    internal = number
    external = number
    protocol = string
  }))
  default = [
    {
      internal = 8300
      external = 8300
      protocol = "tcp"
    }
  ]
}

variable "person_with_address" {
  type = object({
    name = string,
    age = number,
    address = object({
      line1 = string,
      line2 = string,
      county = string,
      postcode = string
    })
  })
  default = {
    name = "Jim"
    age = "21"
    address = {
      line1 = "1 the road"
      line2 = "St Ives"
      county = "Cambridgeshire"
      postcode = "CB1 2GB"
    }
  }
}
```

```terraform
resource "aws_instance" "server"
  root_block_device {
    delete_on_termination = var.disk.delete_on_termination
    encrypted = var.disk.encrypted
    volume_size = var.disk.volume_size
    volume_type = var.disk.volume_type
  }
}

output "person_line1" {
  value = var.person_with_address["address"]["line1"]
}

output "person_name" {
  value = var.person_with_address["name"]
}
```

- `terraform.tfvars file`

```terraform
disk = {
  delete_on_termination = false
  encrypted = true
  volume_size = "20"
  volume_type = "standard"
}
```

</details>

<br>

## variables: map <a id='14c'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
variable "amis" {
  type = map(any)
  default = {
    "us-east-1" : "ami-09d56f8956ab235b3"
    "us-east-2" : "ami-0aeb7c931a5a61206"
  }
}

variable "region" {
  type = string
}

variable "my_map" {
  type = map(number)
  default = {
    "alpha" = 2
    "bravo" = 3
  }
}

variable "my_map" {
  type = map(string)
  default = {
    "alpha" = "ALPHA"
    "bravo" = "BRAVO"
  }
}

variable "ami_ids" {
  type = map
  description = "AMI ID's to deploy"
  default = {
    linux = "ami-0d398eb3480cb04e7"
    windows = "ami-0afb7a78e89642197"
  }
}

variable "os_type" {
    description = "OS to deploy, Linux or Windows"
    type = string
}
```

```terraform
resource "aws_instance" "web" {
  ami = var.amis[var.region]
}

resource "aws_instance" "server" {
  ami = lookup(var.ami_ids, var.os_type, null)
}

# for all values
output "map" {
  value = var.my_map
}

output "alpha_value" {
  value = var.my_map["alpha"]
}
```

- `terraform.tfvars file`

```terraform
region = "us-east-1"
os_type = "linux"
```

</details>

<br>

## variables: number <a id='14d'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
variable "num"{
  type  = number
  default = 123
}

variable "asg_max_size" {
  type    = number
  default = 2
}
```

```terraform
output "num_value" {
  value = var.num
}

resource "aws_autoscaling_group" "asg" {
  max_size = var.asg_max_size


}
```

</details>

<br>

## variables: list(string) <a id='14e'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
variable "availability_zones" {
  type = list(string)
}

variable "security_group_ids" {
    description = "Security group IDs assigned to the EC2 Instance"
    type = list(string)
}
```

```terraform
resource "aws_subnet" "subnet1" {
  availability_zone = var.availability_zones[0]
}

resource "aws_subnet" "subnet2" {
  availability_zone = var.availability_zones[1]
}

resource "aws_instance" "server" {
    vpc_security_group_ids = var.security_group_ids
}
```

- Defining the variable

```terraform
module "webserver" {
  security_group_ids = [aws_vpc.prod.default_security_group_id]
}
```

- `terraform.tfvars` file

```terraform
availability_zones = ["us-east-1a", "us-east-1b"]
```

</details>

<br>

## variables: list(map) <a id='14f'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform
variable "ebs_block_device" {
  description = "Additional EBS block devices to attach to the instance"
  type        = list(map(string))
  default     = []
}
```

```terraform

  # Dynamic blocks can be used for resources that contain repeatable configuration blocks.
  # Instead of repeating several ebs_block_device blocks, a dynamic block is used to simplify the code.

  # This is done by combining the dynamic block with a for_each loop inside.
  # The first line inside the dynamic block is the for_each loop.
  # The loop is iterating through the list of the ebs_block_device variable, which is a list of maps.

  # In the content block, each value of the map is referenced using the lookup function.
  # The logic here is to look for a value in the map variable and if it's not there, set the value to null.
  # The dynamic block will iterate through each map in the list:

resource "aws_instance" "server" {
  #dynamic block with for_each loop
  dynamic "ebs_block_device" {
  for_each = var.ebs_block_device
    content {
    delete_on_termination = lookup(ebs_block_device.value, "delete_on_termination", null)
    device_name           = ebs_block_device.value.device_name
    encrypted             = lookup(ebs_block_device.value, "encrypted", null)
    iops                  = lookup(ebs_block_device.value, "iops", null)
    kms_key_id            = lookup(ebs_block_device.value, "kms_key_id", null)
    snapshot_id           = lookup(ebs_block_device.value, "snapshot_id", null)
    volume_size           = lookup(ebs_block_device.value, "volume_size", null)
    volume_type           = lookup(ebs_block_device.value, "volume_type", null)
    }
}
}
```

```terraform
module "server" {
  ebs_block_device = [
    {
    device_name = "/dev/sdh"
    volume_size = "4"
    volume_type = "standard"
    delete_on_termination = "true"
    },
    {
    device_name = "/dev/sdj"
    volume_size = "4"
    volume_type = "standard"
    delete_on_termination = "true"
    }
  ]

}
```

</details>

<br>

## variables: template <a id='14'></a> ([go to top](#top))

<details>
<summary> Expand For Details </summary>
<br>

```terraform

```

```terraform

```

- `terraform.tfvars file`

```terraform

```

</details>

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

```

```

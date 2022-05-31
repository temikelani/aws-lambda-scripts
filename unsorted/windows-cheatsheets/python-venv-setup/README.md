# Run AWS Linux CLI Commands Using Python Virtual Environment on Windows <a id ='top'></a>

<br>
<br>

# Contents

- [Overview](#0)
- [Set Execution Policy](#1)
- [Create VENV](#2)
- [Syntax](#3)
- [go to top](#top)

<br>
<br>

# Overview <a id='0'></a> ([go to top](#top))

AWS CLI on Windows Powershell has a different set of commands (than teh linux ones). Youc an learn these commands or you can use apython venv to run the linux commands in powershell.

- [Python virtual environment](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html)
- [AWS CLI v1 Venv Setup](https://docs.aws.amazon.com/cli/v1/userguide/install-virtualenv.html)
<br>
<br>
<br>

# Set Execution Policy <a id='1'></a> ([go to top](#top))

- [Fix Execution Policy](https://windowsreport.com/powershell-run-scripts-disabled/)

On windows before you can run a pyhton venv you might have to ser your powershell execution policy to Unrestricted. This will allow you run .ps1 scripts.

- run
    ```
    Get-ExecutionPolicy
    ```
- If the policies are undefined or restricted, run the block below 
    ```
    Set-ExecutionPolicy Unrestricted
    ```

<br>
<br>
<br>

# Create Venv <a id='2'></a> ([go to top](#top))

Navigate to the directory you want to create the vritual environement and run

  ```
  py -m venv enter-name-of-v-env-here
  ```

- Navivate to `name-of-v-env-here/Scripts` and run

  ```
  Activate.ps1
  ```

- Install AWS CLI and configure with `pip install awscli` and `aws configure`

<br>
<br>
<br>


# Syntax <a id='3'></a> ([go to top](#top))

- For a python venv running in powershell use backticks (`) or enter the command in one line

  ```
  aws ec2 run-instances `
  --image-id enter-ami-id-here  `
  --count 1  `
  --instance-type t2.micro `
  --key-name enter-kp-name=here `
  --security-group-ids enter-sg-id-here `
  --subnet-id subnet-10e0727b
  ```

  or

  ```
  aws ec2 run-instances --image-id enter-ami-id-here --count 1 --instance-type t2.micro --key-name enter-kp-name=here --security-group-ids enter-sg-id-here --subnet-id subnet-10e0727b
  ```

<br>
<br>
<br>

# Resources <a id='resources'></a> ([go to top](#top))

- [Python virtual environment](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html)
- [AWS CLI v1 Venv Setup](https://docs.aws.amazon.com/cli/v1/userguide/install-virtualenv.html)
- [Fix Execution Policy](https://windowsreport.com/powershell-run-scripts-disabled/)

<br>
<br>
<br>


// Sample Title

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

[Documentation]()

<br>
<br>
<br>

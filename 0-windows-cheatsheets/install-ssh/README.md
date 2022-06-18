# Install SSH on Windows <a id ='top'></a>

<br>
<br>

# Contents

- [Install SSH on Windows](#0)
- [Resources](#resources)
- [Useful CLI Reference](#CLI)
- [To Do](#to-do)
- [go to top](#top)

<br>
<br>

# Install SSH on Windows <a id='0'></a> ([go to top](#top))

- [Install OpenSSH on Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)

- To install `Open SSH`, `run powershell as admin`

- Run the block below to see if openSSH CLient & Server are installed

  ```
  Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
  ``` 

- run the block below to install them

  ```
  # Install the OpenSSH Client
  Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

  # Install the OpenSSH Server
  Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
  ```

- Start & Configure OpenSSH Server

  ```
  # Start the sshd service
  Start-Service sshd

  # Set the sshd service to be started automatically
  Set-Service -Name sshd -StartupType 'Automatic'
  ```

<br>
<br>
<br>


# Resources <a id='resources'></a> ([go to top](#top))

- [Install OpenSSH on Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)
- []()


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

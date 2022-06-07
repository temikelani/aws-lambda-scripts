# Ansible Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [CLI : Call Playbook](#1)
- [Ansible Config : Host Key Checking](#2)
- [Apt: Update/Upgrade](#3)
- [Apt: Remove Unnecessary Dependencies](#4)
- [Node: Install Dependencies](#5)
- [Create Directory](#6)
- [Copy Files](#7)
- [Run Shell Commands](#8)
- [Main.yml](#9)
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


# CLI : Call Playbook <a id='1'></a> ([go to top](#top))

  ```bash
  ansible-playbook -i `path-to/inventory.txt` `path-to/main.yml` --private-key=`path-to/private-key.pem`
  ```
<br>
<br>
<br>

# Ansible Config : Host Key Checking <a id='2'></a> ([go to top](#top))
  
  ```cfg
  [defaults]
  host_key_checking = False
  ```



<br>
<br>
<br>

# Apt Update/Upgrade Packages <a id='3'></a> ([go to top](#top))

  ```yml
  ---
  - name: "update apt packages"
    become: true
    become_method: sudo
    apt:
      update_cache: yes
      

  - name: "upgrade packages"
    become: yes
    apt:
      upgrade: yes
  ```


<br>
<br>
<br>

# Apt: Remove Unnecessary Dependencies <a id='4'></a> ([go to top](#top))

  ```yml
  ---
  - name: "Remove dependencies that are no longer required"
    become: true
    apt:
      autoremove: yes
  ```

<br>
<br>
<br>

# Apt: Node Install Dependencies <a id='5'></a> ([go to top](#top))

  ```yml
  ---
  - name: "install dependencies."
    become: yes
    apt:
      name: ["nodejs", "npm"]
      state: latest
      update_cache: yes
  ```


<br>
<br>
<br>

# Create Directory <a id='6'></a> ([go to top](#top))

```yml
---
- name: Creates directory
  file:
    path: ~/web
    state: directory
```

<br>
<br>
<br>

# Copy Files <a id='7'></a> ([go to top](#top))

  ```yml
  ---
  - name: Copy index test page
    template:
      src: "files/index.js"
      dest: "~/web/index.js"
  ```
  ```yml
  ---
  - name: "Install index.html page"
  copy:
    src: index.html
    dest: /var/www/html/index.html
    backup: yes
  ```

<br>
<br>
<br>

# Run Shell Commands <a id='8'></a> ([go to top](#top))

```yml
---
- name: Executing node
  shell: |
    pm2 start ~/web/index.js -f
```

```yml
---
- name: Print env variable
  shell: echo $PATH
  register: print_result

- name: print message
  debug:
    msg: "{{ print_result.stdout_lines }}"
```

<br>
<br>
<br>

# Main.yml <a id='9'></a> ([go to top](#top))

```yml
---
- name: 12-Remote Control Using Ansible
  hosts: all
  user: ubuntu
  become: true
  become_method: sudo
  become_user: root
  roles:
    - prepare
    - apache
    - setup
```


<br>
<br>
<br>

# Install Apache <a id=''></a> ([go to top](#top))

```yml
---
- name: "Install Apache2"
  become: true
  apt:
    name: ["apache2"]
    state: latest
    update_cache: yes

- name: "Install index.html page"
  copy:
    src: index.html
    dest: /var/www/html/index.html
    backup: yes
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


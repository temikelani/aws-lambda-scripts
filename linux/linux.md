# ... Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [Essential Commands](#com)
  - [ls](#1)
  - [cd](#2)
  - [pwd](#3)
  - [mkdir](#4)
  - [touch](#5)
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
  - [cat, tar, exit, less, q, man, stat](#20)
- [Package Managers & Installations](#)
  - [](#)
  - [](#)
- [Vim](#)
  - [](#)
  - [](#)
- [Accouts, Users, Groups, Ownership & Permissions](#)
  - [](#)
  - [](#)
  - [](#)
  - [umask, ](#)
- [Bash Scripting](#)
  - [](#)
  - [](#)
- [Tips & Tricks](#tip)
  - [Multple commands](#)
  - [space between commands](#)
  - [](#)
  - [](#)
- [Environmental Variables](#)
  - [](#)
  - [](#)
- [Networking](#)
  - [](#)
  - [](#)
- [SSH](#)
  - [](#)
  - [ssh, scp, ](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [go to top](#top)

<br>
<br>
<br>

# Essential Commands <a id='com'></a> ([go to top](#top))

<details>
<summary> Expand to see commands </summary>
</details>

<br>

## `ls` <a id='1'></a> ([go to top](#top))

<details>

<summary>list the contents of the current directory</summary>

- [Documentation](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/)
- run `ls` to see all the contents of the current directory
- run `ls -r` to sort contents in reverse order
- run `ls [path to dir]` to see the contents of the `dir` directory
- run `ls ~` to see the contents of the `home` directory
- run `ls /` to see the contents of the `root` directory
- run `ls ~ / [enter-path-to-dir]` to see the contents of the `home directory`, `root` and `dir` directory`
- run `ls -l` to see the contents of the current dir in long format... long format shows you the `permissions`
- run `ls -t` to see the files listed in order of modification time
- run `ls -lt` to see in long format the files in order of last modification time
- run `ls -a` to list all files (including hidden ones)
- run `ls -S` to sort list by size
- run `ls -X` to sort aphabeticatally by extension
- run `ls -R` to list sub-directories recursively
- run `ls -alt` to see combine all the previous options
</details>

<br>

## cd <a id='2'></a> ([go to top](#top))

<details>
<summary>change the working directory</summary>

- [Documentation](https://linuxize.com/post/linux-cd-command/)
- run `cd [path to dir]` to change the directory to `dir` directory
- run `cd .` to change to the `current` directory (essentially no change)
- run `cd ..` to change to the `parent` directory
- run `cd ../..` to change to the `grandparent` directory
- run `cd ~ to change to the `home` director of the current user
- run `cd /` to change to the the `root` directory
- run `cd /bin` to change to the `bin` directory in the `root` folder
- run `cd ~[username]` to navigate to another user's (`username`) home directory
- run `cd 'dir with space in its name'` to naviagte to a directory with spaces in its name
</details>

<br>

## `pwd` <a id='3'></a> ([go to top](#top))

<details>
<summary>view the current working directory</summary>

- [Documentation](https://linuxize.com/post/current-working-directory/)
- run `pwd` to see what directory you're currently in
</details>

<br>

# mkdir <a id='4'></a> ([go to top](#top))

<details>
<summary>create a directory</summary>

- [Documentation](https://linuxize.com/post/how-to-create-directories-in-linux-with-the-mkdir-command/)
- run `mkdir newdir` to create the directory `newdir`
- run `mkdir /tmp/newdir` to create a directory `newdir` in the `/tmp` directory
- run `mkdir -p /home/linuxize/Music/Rock/Gothic` to create the directory `Gothic` in that path
- run `mkdir -p /home/linuxize/Music/Rock/Gothic` if the parent directories do not exist
- run `mkdir -m 700 newdir` to create the directory `newdir`
- run `mkdir dir1 dir2 dir3` to create multiple directories
- run `mkdir -p Music/{Jazz/Blues,Folk,Disco,Rock/{Gothic,Punk,Progressive},Classical/Baroque/Early}` to create a directory tree
</details>

<br>
<br>
<br>

# touch <a id=''></a> ([go to top](#top))

<details>
<summary>Update the timestamps on existing files and directories as well as creating new, empty files.</summary>

- [Documentation](https://linuxize.com/post/linux-touch-command/)
- run `touch file1` to create `file1` if it doesn't already exist
- run `touch file1 file2 file3` to create multiple files
</details>

<br>
<br>

# wildcards <a id=''></a> ([go to top](#top))

- `*` to select all files
- `g*` to select any files starting with `g`
- `b*.txt` to select any files starting with `b` and ends in `.txt`
- `data???` to select any files beginning `data`
- `[abc]*` to select any files starting with an `a,b or c`
- `backup.[0-9][0-9]` to selct any files starting with `backup.` and ending with 2 numerals
- `[[:upper]]*` to select any files starting with an uppercase
- `[![:digit]]*` to select any files that do not begin with a numeral
-

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

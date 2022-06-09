# Linux Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [Essential Commands](#com)
  - [ls](#ls)
  - [cd](#cd)
  - [pwd](#pwd)
  - [mkdir](#mkdir)
  - [touch](#touch)
  - [wildcards](#*)
  - [rm](#rm)
  - [mv](#mv)
  - [cp](#cp)
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
  - [cat, tar, exit, less, q, man, grep, date, stat](#20)
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
  - [cron jobs](#)
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
  - [ssh, scp, rsync](#)
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

- Links for later
  - https://github.com/temikelani/cloud-training-path/tree/main/linux/nana-bootcamp
  - https://github.com/temikelani/cheatsheets/blob/main/linux/linux.md
  - https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/
    <br>

## `ls` <a id='ls'></a> ([go to top](#top))

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

## cd <a id='cd'></a> ([go to top](#top))

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

## `pwd` <a id='pwd'></a> ([go to top](#top))

<details>
<summary>view the current working directory</summary>

- [Documentation](https://linuxize.com/post/current-working-directory/)
- run `pwd` to see what directory you're currently in
</details>

<br>

## mkdir <a id='mkdir></a> ([go to top](#top))

<details>
<summary>create a directory</summary>

- [Documentation](https://linuxize.com/post/how-to-create-directories-in-linux-with-the-mkdir-command/)
- run `mkdir newdir` to create the directory `newdir`
- run `mkdir /tmp/newdir` to create a directory `newdir` in the `/tmp` directory
- run `mkdir -p /home/linuxize/Music/Rock/Gothic` to create the directory `Gothic` in that path
- run `mkdir -p /home/linuxize/Music/Rock/Gothic` if the parent directories do not exist
- run `mkdir -m 700 newdir` to create the directory `newdir` with `700` permissions
- run `mkdir dir1 dir2 dir3` to create multiple directories
- run `mkdir -p Music/{Jazz/Blues,Folk,Disco,Rock/{Gothic,Punk,Progressive},Classical/Baroque/Early}` to create a directory tree
</details>

<br>

## touch <a id='touch'></a> ([go to top](#top))

<details>
<summary>Update the timestamps on existing files and directories as well as creating new, empty files.</summary>

- [Documentation](https://linuxize.com/post/linux-touch-command/)
- run `touch file1` to create `file1` if it doesn't already exist
- run `touch file1 file2 file3` to create multiple files
</details>

<br>

## wildcards <a id='*'></a> ([go to top](#top))

<details>
<summary> Select all that meet the criteria </summary>

- usage; `ls | grep *` `ls | grep g*` etc
- `*` to select all `files`
- `g*` to select any `files` starting with `g`
- `b*.txt` to select any `files` starting with `b` and ends in `.txt`
- `data???` to select any `files` beginning `data`
- `[abc]*` to select any `files` starting with an `a,b or c`
- `backup.[0-9][0-9]` to selct any `files` starting with `backup.` and ending with 2 numerals
- `[[:upper]]*` to select any `files` starting with an uppercase
- `[![:digit]]*` to select any `files` that do not begin with a numeral

</details>

<br>

## rm <a id='rm'></a> ([go to top](#top))

<details>

<summary> Delete a file or directory</summary>

- [Documentation](https://linuxize.com/post/rm-command-in-linux/)
- usage: `rm [OPTIONS]... FILE...`
- run `rm filename` to delete a file
- run `rm -v filename` to get info on what;s being removed
- run `rm -f filename` r to not prompt the user and to ignore nonexistent files and arguments.
- run `rm filename1 filename2 filename3` to remove multiple files
- run `rm *.png` to remove all files ending with `.png`
- run `rm -d dirname` or `rmdir dirname` to remove an empty directory
- run `rm -r dirname` to remove non-empty directories
- run `rm -i filename1 filename2` to prompt the user before removal
  - `rm -i filename1 filename2 filename3 filename4`
- run `rm -rf dirname` to remove a diretory without being prompted

</details>

<br>

## mv <a id='mv'></a> ([go to top](#top))

<details>

<summary> Move/Rename a file or directory </summary>

- [Documentation](https://linuxize.com/post/how-to-move-files-in-linux-with-mv-command/)
- usage: `mv [OPTIONS] SOURCE DESTINATION`
  - The `SOURCE can be one, or more files or directories`, and `DESTINATION can be a single file or directory`.
- run `mv file1 /tmp` to move the file file1 from the current working directory to the /tmp directory
- run `mv -i file1 /tmp` to be prompted before overwiting if the destination `file1` already exists
- run `mv -f file1 /tmp` to not be prompted
- run `mv -n file1 /tmp` to never overwrite an existing file
- run `mv -b file1 /tmp` to create a backup of the destination file if it exists
  - The backup file will have the same name as the original file with a tilde (~) appended to it.
- run `mv file1 file2` To rename a `file1` as `file2` (assuming `file2` doesn't exist)
- run `mv dir1 dir2`
  - `if the dir2 directory exists`, the command will `move dir1 inside dir2`.
  - `If dir2 doesn’t exist`, `dir1 will be renamed to dir2`:
- run `mv file1 file2 dir1` to move the files `file1` and `file2` to the `dir1` directory
- run `mv *.pdf ~/Documents` to move `all pdf files` from the `current directory` to the `~/Documents directory`

</details>

<br>

## cp <a id='cp'></a> ([go to top](#top))

<details>

<summary> Move/Rename a file or directory </summary>

- [Documentation](https://linuxize.com/post/how-to-copy-files-and-directories-in-linux/) || [and](https://linuxize.com/post/cp-command-in-linux/)
- usage: `cp [OPTIONS] SOURCE... DESTINATION`
- run `cp file file_backup` to copy a file named file.txt to file_backup.txt
- run `cp file.txt /backup` to copy the file file.txt to the /backup directory
- run `cp file.txt /backup/new_file.txt` to copy the file to the specified directory as new_file.txt
- By default, if the destination file exists, it is overwritten. `The -n option tells cp not to overwrite an existing file.`
- run `cp -i file.txt file_backup.txt` to force a prompt
- run `cp -R Pictures Pictures_backup` to copy a directory, including all its files and subdirectories, use the -R or -r option.
  - `we are copying the directory Pictures to Pictures_backup`
- run `cp -RT Pictures Pictures_backup` to copy only the files and subdirectories but not the source directory,
  - another way is to run `cp -RT Pictures/* Pictures_backup/`
  - however it does not copy the hidden files and directories (the ones starting with a dot .):
- run `cp file.txt dir file1.txt dir1` to copy multiple files and directories at once
  - specify their names and use the destination directory as the last argument:
- run `cp -p file.txt file_backup.txt` to preserve the file mode, ownership , and timestamps :
  - By default, when using the cp command to copy a file, the new file will be owned by the user performing the command. Use the -p option
- run `cp -v file.txt file_backup.txt` to print what is being done
- run `cp *.png /backup` to copy all png files
- run `rsync -a file.txt file_backup.txt` to copy a single file from one to another location
- run `rsync -a /var/www/public_html/ /var/www/public_html_backup/` to copy a directory:

</details>

<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

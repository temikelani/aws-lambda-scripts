# ... Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [`git init` - create new repo](#1)
- [`.gitignore` - reset git ignore](#2)
- [`.gitignore` - custom git ignore](#3)
- [`git diff`](#4)
- [`git commit`](#5)
- [`git log`](#6)
- [`HEAD`, `git checkout`, `git reset` and backtracking](#7)
- [`git stash` ](#8)
- [`git alias`](#9)
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

# `git init` - create new repo <a id=''></a> ([go to top](#top))

- Create a new repo `new-repo`

  ```bash
  cd new-repo
  git init
  git add .
  git commit -m "first commit"
  git branch -M main
  git remote add origin https://github.com/temikelani/new-repo.git
  git push -u origin main
  ```

<br>
<br>
<br>

# `.gitignore` - reset git ignore <a id=''></a> ([go to top](#top))

```
git rm -rf --cached .
git add .
```

<br>
<br>
<br>

# `.gitignore` - custom git ignore <a id='3'></a> ([go to top](#top))

```
*.cer
*.pem
*.ppk
**/node_modules/

*new_user_credentials.csv

**/.terraform/*
*.tfstate
*.tfstate.*
crash.log
override.tf
override.tf.json
*_override.tf
*_override.tf.json

*.DS_Store
*.ipynb_checkpoints
```

<br>
<br>
<br>

# `git diff` <a id='4'></a> ([go to top](#top))

- `git diff` shows changes between recent (uncommited) changes and the last commit/staging area
- You can check the differences between the working directory and the staging area/last commit with

```
git diff
```

<br>
<br>
<br>

# `git commit` <a id='5'></a> ([go to top](#top))

- A commit permanently stores changes from the staging area inside the repository.

- `git commit` tells Git to take a snapshot (record) of all added content at this point. Youb must add a message to decribe the resent changes

  - run `git commit -m "enter-commit-message-here"` to commit changes
  - run `git commit -a -m "Another message"` or `git commit -am "Another message"` to add/stage all changes and commit at the same
    - it will not add/stage new files, only modified files
  - run `git commit --amend` to modify the last commit with the current changes
  - run `git commit --amend --no-edit` to kepe the same commit message

  <hr>
  <br>

- remove the latest commit run

  ```
  git checkout HEAD^
  git branch -f master
  git checkout master
  git log
  ```

  use `git reflog` to retrieve it

  <hr>
  <br>

- Standard Conventions for Commit Messages:
  - Must be in quotation marks
  - Written in the present tense
  - Should be brief (50 characters or less) when using -m
  - `ADD More git commit convenstions`

<br>
<br>
<br>

# `git log` <a id='6'></a> ([go to top](#top))

- Often with Git, you’ll need to refer back to an earlier version of a project.
- Commits are stored chronologically in the repository and can be viewed with:
- `git log` shows the the history of this repository. `git log path-to-file` to see the history of a specific file
  - it containes the commits made and their hashes
  - Hit `q to stop viewing it`, and return to the command line
  - run `git log --oneline` to view the log is `one line per commit`
  - run `git log -S "keyword"` displays a list of commits that contain the keyword in the message.
  - run `git log --oneline --graph` to get a visual representation of the history
  - run `git log --decorate --graph --oneline` for useful information about the reference names (branches and tags) at various commit points.
  - run `git log --decorate --graph --oneline --all` to show logs for all branches
  - run `git log --pretty=format:"%h %s" --graph` to use regex????

<br>
<br>
<br>

# HEAD, `git checkout`, `git reset` and Backtracking <a id='7'></a> ([go to top](#top))

- In Git, the commit you are currently on is known as the `HEAD commit`. `In many cases, the most recently made commit is the HEAD commit`.

```bash
git show HEAD
```

- If you `MADE` a change on a file `filename`
- `AND HAVE NOT COMMITED IT`
- but want to discard that change run `THE BLOCK BELOW`
- It will `restore the file in your working directory` to `look exactly as it did when you last made a commit.`
- All changed that deviate from the commit will be instantly removed

```bash
git checkout HEAD filename
```

- or

```bash
git checkout -- filename
```

- or for a specific commit

```bash
git checkout commit_SHA
```

- If you `DELETED`/`MADE` a change on a file `filename`
- `AND HAVE STAGED IT BUT NOT COMMITED IT`
- but want to discard that change run `THE BLOCK BELOW`
- It will `unstage that file from the staging area`
- `IT WILL RESET the file in the STAGING AREA` to be the `same as the HEAD commit`.
- `It WILL NOT` `discard file changes from the working directory`, it `just removes them from the staging area.`
- Use `git status` before and after running to see difference

```bash
git reset HEAD filename
```

- If you `MADE` a change on a file `filename`
- `AND HAVE COMMITED IT`
- but want to discard that change
- `Without affecting the working directory`
  - `It WILL NOT` `discard file changes from the working directory`, it `just removes them from the staging area.`
- run `THE BLOCK BELOW`
- verify with `git diff` that your repo is back to the specified commit
- commit_SHA = first 7 characters of the SHA of a previous commit
- commit_SHA now becomes `new HEAD`

```bash
git reset commit_SHA
```

- `GIT RESET IS USEFUL WHEN WANT TO PRESERVE CHANGES BUT YOU DO NOT WANT THEM OR THE CHANGES IN A CERTIAN FILE TO BE PART OF THE NEXT COMMIT (STAGING AREA)`

<br>
<br>
<br>

# `git stash` <a id='8'></a> ([go to top](#top))

[`git stash`](https://git-scm.com/docs/git-stash)

- Let’s say you’re working on experimental code on a fresh branch and realize that you forgot to add something to a previous commit in order to continue your work. In order to go to a different branch, one must always be at a clean commit point. In this case you don’t want to commit your experimental code since it’s not ready but you also don’t want to lose all the code you’ve been working on.
- A good way to handle this is by using git stash, which allows you to get back to a clean commit point with a synchronized working tree, and avoid losing your local changes in the process. You’re “stashing” your local work temporarily in order to update a previous commit and later on retrieve your work.

<hr>
<br>

```
    [do some work]
    [get interrupted]
    git stash
    [deal with interruption]
    git stash pop
```

`git stash` saves your local modifications away and reverts the working directory to match the HEAD commit. (most recent commit)

- make a change after a commit you're unsure of and dont want to commit yet
- run `git stash` to store those changes away and restore to the HEAD (tag if you like)
- run `git status` to confirm there are not changed betwween HEAD and you local repo
- run `git log` to see what happened
- run `git stash list` to see all stashes
- run `git stash pop` to re-apply the 0 index stash and remove it from the stash list.
- run `git diff` to confirm stash has been reapplied
- run `git stash show --patch stash@{n}` where n is a number 0,1,2,3... on the stash list to see what changes were made in what stash
- run `git stash apply stash@{n}` to apply a specific stash, whenre n is the index of the stash. while pop removes the stash form the list, apply does not.
- run `git stash drop stash@{n}` to drop a stash

<br>
<br>
<br>

# `git alias` <a id='9'></a> ([go to top](#top))

- If you have a set of commands that you use regularly and want to save some time from typing them, you can easily set up an alias for each command using Git config.

```bash
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.glop "log --pretty=format:"%h %s" --graph"
```

- now you can run

```bash
$ git co example_branch
```

- instead of git checkout example_branch
  <br>
  <br>
  <br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

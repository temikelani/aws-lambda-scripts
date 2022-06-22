# ... Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [Create New Repo](#1)
- [Reset Git ignore](#2)
- [Custom Git Ignore](#3)
- [`git diff`](#4)
- [`git commit`](#5)
- [`git log`](#6)
- [HEAD, `git checkout`, `git reset` and Backtracking ](#7)
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

# Create New Repo <a id=''></a> ([go to top](#top))

- Create a new repo `new-repo`

  ```bash
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

# Reset Git ignore <a id=''></a> ([go to top](#top))

```
git rm -rf --cached .
git add .
```

<br>
<br>
<br>

# Custom Git Ignore <a id='3'></a> ([go to top](#top))

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

- If you have added a file to the staging area with

```
git add .
```

- but have made a change since adding it. You can check the differences between the working directory and the staging area w

```
git diff
```

<br>
<br>
<br>

# `git commit` <a id=''></a> ([go to top](#top))

- A commit permanently stores changes from the staging area inside the repository.
- Standard Conventions for Commit Messages:
  - Must be in quotation marks
  - Written in the present tense
  - Should be brief (50 characters or less) when using -m
  - `ADD More git commit convenstions`

```
git commit -m "Complete first line of dialogue"
```

<br>
<br>
<br>

# `git log` <a id=''></a> ([go to top](#top))

- Often with Git, you’ll need to refer back to an earlier version of a project.
- Commits are stored chronologically in the repository and can be viewed with:

```
git log
```

<br>
<br>
<br>

# HEAD, `git checkout`, `git reset` and Backtracking <a id=''></a> ([go to top](#top))

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

- If you `MADE` a change on a file `filename`
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

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

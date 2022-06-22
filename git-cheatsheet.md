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
- [HEAD and Backtracking](#7)
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

# HEAD and Backtracking <a id=''></a> ([go to top](#top))
- In Git, the commit you are currently on is known as the `HEAD commit`. `In many cases, the most recently made commit is the HEAD commit`.

```bash
git show HEAD
```

- If you commited a change onf a file `filename` but want to discard that change run

```bash
git checkout HEAD filename
```

- It will restore the file in your working directory to look exactly as it did when you last made a commit.

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

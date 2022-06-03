# Dumble
Play Dumble or simulate games with Python

## Install project

Download files
```console
~$ git clone https://github.com/WildSiphon/Dumble.git
~$ cd Dumble
```

Create a virtual environment and source it
```console
~$ python3 -m venv venv-dumble
~$ source venv-dumble/bin/activate
```

Download requirements
```console
~$ pip install -r requirements.txt
```

Install pre-commit hooks
```console
~$ pre-commit install
```

## Using GitHub

Show current local branch (use `-a` to see all local and remote branch).
```console
~$ git branch -a
* main
```

Change current branch (use `-b` to create the branch you want to move in).
```console
~$ git checkout ${BRANCH_NAME}
```

Verify that you created a new branch and selected it.
```console
~$ git branch -a
* ${BRANCH_NAME}
  main
```

Now you will work on this branch without modifying the main one.
```console
~$ git add -A     # Add every file to list files that must be updated
~$ git commit -a  # Save all your changes
~$ git push       # Upload your changes to the project hub
```

You just need to do a merge request when you consider your work and your branch
over.

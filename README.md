# Project Initialization Automation

This project is based on [Kalle Hallden's repository](https://github.com/KalleHallden/ProjectInitializationAutomation) to automate project initialization, by creating a local repository, a repository at GitHub and synchronize both.<br>In my case, as I am using GitLab I just had to adapt some procedures.

The procedures to be automated with the script are basically:
- navigate to my Workspace folder (directory)
- type the command:
> create <*project_name*>
- create a project with the *project_name*
- navigate to the *project_name* folder
- git init
- git remote set-url origin https://gitlab.com/*username*/*project_name*
- create a blank README.md file
- git add
- git commit -m 'Initial commit'
- git push origin master
- code .

### GitLab access
Of Course, I had to replace the Kalle PyGithub package with an equivalent for GitLab.
I am using the awesome [*python-gitlab*](https://python-gitlab.readthedocs.io/en/stable/index.html) package instead.


### Install: 
```bash
git clone "https://gitlab.com/rhkina/project-init-automation.git"
cd project-init-automation
pip install -r requirements.txt
touch .env
Then open the .env file and store your username, password, and desired file destination. Use the provided format at the bottom of this README.
source ~/.my_commands.sh
```

### Usage:
```bash
To run the script type in 'create <project_namer>'
```
A folder with the project_name will be created inside the path specified inside the .env file (the FILEPATH variable).

### Env File Format:
Access [GitLab](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) Docs to see how to generate your access token.
```bash
TOKEN="token_from_gitlab"
FILEPATH="/path/to/your/project/folder/"
```

### Create an executable
To generate an executable from create.py run the command:
```
pyinstaller --onefile create.py
```
The executable will be created at *dist* folder.
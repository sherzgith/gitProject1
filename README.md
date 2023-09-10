# Git and Github

git - local version control system
gitHub - cloud repository  website, website that is integrated with git system,
shareable repository/location, that produce shareable link

Git
- local vs cloud (github)
- create project -> enable git (enable VCS) -> define cloud -> add the cloud link (add origin)
    -> create repository on the GitHub -> use the link as origin
    -> configure global git configuration (name,email)
    -> add file (select files) and commit , push, pull

1. Git commands(in Git Bash) you will use for local project:
    cd projectDirectory
    git init
    git add folder1/scenario1.py
    git commit -m 'message for your commit'
    git status
    git log
    git push
    git pull

2. Branching :
    Create new branch, switch to new branch, create Pull Requests (highlights the change)
    a. Create new local branch :
        1 - Pycharm :
            Select new branch option for the current branch (bottom right)
            push each branch separately, creates origin : feature1-scene1 automatically
        2 - git bash, git CLI (command line interface):
            git checkout -b 'new-branch-name'
            git add folder1/ scenario1.py
            git commit -m 'message for your commit'
            git push
            git push --set-upstream origin feature1-scen2
    b. Collaboration in GitHub :
        a. Creating the Pull Requests, get reviews and approval from Sr.Engineer
        b. Merge your code in your branch to a master(main) branches



3. Get/download gitHub project to your local location and start new project:
    cd /C/dev
    mkdir temp
    pwd
      C/dev/temp
    git clone https://github.com/sherzgith/gitProject1.git
    cd gitProject1
    git log # shows the latest commit in the log
    # then you can open in the PyCharm start working on it as regular project

- Ignore files
    - create .gitignore ( list of files to be ignored by git)
    you can copy the standard .gitignore file for python projects( like we did in the class)

---
# MD (Markdown ) files for Project Documentation
README files are previewed in GitHub projects bt default, so usually README files are created in 
Markdown language so text format looks more readable and neat , links, images can be also included
in the document.( Most of the functionalities you could do in MS Word or other text Editors )
Markdown language is mostly used to write technical texts.


## two hashtags are Heading 2
### two hashtags are Heading 3
#### two hashtags are Heading 4

**marking the text as bold**

*italic text is covered with asterisk*

## Below you can see the bullet points:
- point 1 of many points
- point 2 of many points
- point 3 of many points

## Highlight the code or commandline

You can highlight the code with apostrophe (`) or with 
indentation:

```python
print('Python code inside the code block in MD file')
```
```Shell
pwd
cd /c/dev/
mkdir "gitProject1"
# command line for the shell
cd gitProject1
```

b. Indent the line to put in code box 
    
    print('my project')

## Displaying links in MD file

Please [click here](https://www.jetbrains.com/help/pycharm/markdown.html) 
to see more details about md features.

## Displaying the picture in md file

You can see the picture below

![messipic](./data/Lionel-Messi-PNG-Picture.png)



Picture will be between the text

## References:
1. Sherzod's GitHub account [link](https://github.com/sherzgith)

2. [Markdown support](https://www.jetbrains.com/help/pycharm/markdown.html)








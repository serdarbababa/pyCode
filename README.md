# SERDAR GIT
## How to use git:
Quick setup — if you’ve done this kind of thing before

https://github.com/serdarbababa/Rcode.git


### Create a new repository on the command line

echo "# Rcode" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/serdarbababa/pyCcode.git
git push -u origin master

### push an existing repository from the command line

git remote add origin https://github.com/serdarbababa/pyCcode.git
git push -u origin master


### Benim yaptiklarim
#make a readme file
echo "# Rcode" >> README.md
#initialize
git init
#configure git for user name
git config --global user.name "Serdar B"

#adding files 
git add *.ipynb

#cheking status
git status

#removing files
git rm .ipynb
git rm -f .ipynb_checkpoints/*

#comminting data
git commit 
git commit -a

#pushing data
git push -u origin master

#set active branch on server and push 
git push --set-upstream origin develop

#show branches
git branch

#git swithc branches
git checkout develop



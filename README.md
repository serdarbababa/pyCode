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
#make a readme file<p>
echo "# Rcode" >> README.md<p>
#initialize<p>
git init<p>
#configure git for user name<p>
git config --global user.name "Serdar B"<p>

#adding files <p>
git add *.ipynb<p>

#cheking status<p>
git status<p>

#removing files<p>
git rm .ipynb<p>
git rm -f .ipynb_checkpoints/*<p>
<p>
#comminting data<p>
git commit<p> 
git commit -a<p>
<p>
#pushing data<p>
git push -u origin master<p>

#set active branch on server and push <p>
git push --set-upstream origin develop<p>

#show branches<p>
git branch<p>

#git swithc branches<p>
git checkout develop<p>



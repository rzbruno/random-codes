#!/bin/bash

git init 
touch main.py
git add main.py
git commit -m 'base'

#start new feature
git checkout -b feature
touch feature.py
git add feature.py
git commit -m 'feature: working on'

#bugfix
git checkout master
echo '#bugfix' > main.py
git commit -a -m 'bugfix'

#back to feature
git checkout feature
echo 'feature xyz' > feature.py
git commit -a -m 'feature: done'

#back to master (assuming that it is already updated)
git rebase master
git checkout master
git merge feature

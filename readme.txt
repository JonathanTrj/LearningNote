this is a learn schedule of git

the first step: git init

the second step: git add & git commit -m "descrip"

if changes happened, git status can show the imformation
further, git diff ,,.txt can show the changes

1: change for checkout -- 

2: change for checkout --

3: change for checkout --

git log can show the history record of git commit
further, use git log --pretty=oneline can optimize the result

git reset --hard HEAD^ can return the change to that commit result
further, use git reset --hard ..(hashcode) can return to the specific commit result
further, use git reflog can show the history of your operations

git reset HEAD <file> can dismiss the operate of git add/rm, backward to the word directory
if you want to return the change to last add or commit operate:
	if you haven't git add <file>, then use git checkout -- <file>
	if you habe git add <file>, then use git reset HEAD <file>, after that, use git checkout -- <file>

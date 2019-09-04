this is a learn schedule of git

//init a repository
the first step: git init

//commit operation
the second step: git add & git commit -m "descrip"

//show the status of work place and stage place
if changes happened, git status can show the imformation
further, git diff ,,.txt can show the changes

1: change for checkout -- 

2: change for checkout --

3: change for checkout --

//commit history
git log can show the history record of git commit
further, use git log --pretty=oneline can optimize the result

//backward
git reset --hard HEAD^ can return the change to that commit result
further, use git reset --hard ..(hashcode) can return to the specific commit result
further, use git reflog can show the history of your operations

git reset HEAD <file> can dismiss the operate of git add/rm, backward to the word directory
git checkout -- <file> can replace the file in work directory with the file in repository version(committed version)
if you want to return the change to last add or commit operate:
	if you haven't git add <file>, then use git checkout -- <file>
	if you habe git add <file>, then use git reset HEAD <file>, after that, use git checkout -- <file>
git@github.com:JonathanTrj/LearnGit.git
//remote repository
git remote add repo_name git@github.com:JonathanTrj/(...).git
//push first time
git push -u repo_name branch_name(default is 'master')
//push
git push repo_name branch_name(default is 'master')
//git clone
git clone git@github.com:JonathanTrj/(...).git

//branch
//pointer HEAD point to 'master', and 'master' point to the current node in a branch
//when create and switch to a new branch, the HEAD pointer will point to the new 'branch', and the 'branch' point to the current node of this branch
//when merge the branch with master branch, the HEAD pointer will point to 'master' again.
create and switch to a new branch:
git checkout -b branch_name
equals to: git branch branch_name & git checkout branch_name
git branch can show the list of branches, and current branch will be displayed with a (*)
git merge branch_name can merge the branch_name branch to the current branch
git branch -d branch_name can delete the branch
git switch branch_name is supported by the high version of GIT
//when different branches' files conflict when merge:
git status check for the conflict files and make changes, 
git log --graph can show the branch merge graph
//manage of branch
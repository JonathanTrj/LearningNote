this is a learn schedule of git

//init a repository
the first step: 
	"git init"

//commit operation
the second step: 
	"git add <filename>" & "git commit -m <content>"

//show the status of work place and stage place
if changes happened, 
	"git status"
can show the imformation
further, use 
	"git diff <filename>" 
can show the changes

//commit history
	"git log" 
can show the history record of git commit
further, use 
	"git log --pretty=oneline" 
can optimize the result

//backward
	"git reset --hard HEAD^" 
can return the change to the previous commit result
further, use 
	"git reset --hard <commitID>"
can return to the specific commit result
further, use 
	"git reflog"
can show the history of your operations, which contains all commitID

	"git reset HEAD <file>"
can dismiss the operate of git add/rm(unstage), backward to the word directory
	"git checkout -- <file>"
can replace the file in work directory with the file in repository version(committed version)
if you want to return the change to last add or commit operate:
	if you haven't "git add <file>", then use 
		"git checkout -- <file>"
	if you have "git add <file>", then use 
		"git reset HEAD <file>"
	after that, use:
		"git checkout -- <file>"

//remote repository
	"git remote add repo_name git@github.com:JonathanTrj/<reponame>.git"
//push first time
	"git push -u <repo_name> <branch_name>"
	(default is 'master')
//push
	"git push <repo_name> <branch_name>"
	(default is 'master')
//git clone
	"git clone git@github.com:JonathanTrj/<reponame>.git"
	//the branch defaultly has only "master", if you want to work with another remote branch, then
	"git checkout -b <local_branch_name> <remote_name>/<remote_branch_name>"
//git clone specific branch
	"git clone -b <branch_name> <remote_address>"
//git clone into specific folder
	"git clone <remote_address> <folder_name>"

//branch
//pointer HEAD point to 'master', and 'master' point to the current node in a branch
//when create and switch to a new branch 'branch', the HEAD pointer will point to 'branch', and the 'branch' point to the current node of this branch
//when merge the branch with master branch, the HEAD pointer will point to 'master' again.
create and switch to a new branch:
	"git checkout -b <branch_name>"
equals to: 
	"git branch <branch_name>" 
	&
	"git checkout <branch_name>"
	
	"git branch" 
can show the list of branches, and current branch will be displayed with a (*)
	"git branch -a"
can show the list of branches, including all branches in remote
	"git branch -r"
can show the list of branches in remote only
	"git merge <branch_name>" 
can merge the branch_name branch to the current branch
	"git branch -d <branch_name>" 
can delete the branch
	"git switch <branch_name>" 
is supported by the high version of GIT
//when different branches' files conflict when merge in local environment:
	"git status"
check for the conflict files and make changes, 
	"git log --graph"
can show the branch merge graph
//manage of branch
if you want to keep the commit log of branch merge, then:
	"git merge --no-ff -m <content> <branch_name>"
//if you want to temperary work in another branch with the unfinished work in current branch, then:
	"git stash"
it will temporary storage your current branch works, which makes your current work place clean
	"git stash list" 
can show the list of works
	"git stash apply <stashid>" 
	&
	"git stash drop <stashid>"  
	/
	"git stash pop"
	(this will return your work and delete the stash at the same time)
	
	"git cherry-pick <commitID>"
can copy a commit to current branch
//corporate with team
	"git remote" 
can show the remote repository info
	"git remote -v" 
can show the address of fetch and push
	"git push <repo_name> <branch_name>"
	"git clone ..."
generally, after clone, you can only see the master branch, if you want to work in another branch in remote, then:
	"git checkout -b <branch_name> <remote_repo_name>/<branch_name>"
	"git push <remote_repo_name> <remote_branch_name>"
if conflict with partner, then:
1,conduct a connection from current branch to remote branch
	"git branch --set-upstream-to=<remote_repo_name>/<remote_branch> <current_branch>"
2,git pull
	"git pull"
//git tag
	"git tag <tag_name>" 
	/
	"git tag <tag_name> <commitID>"
	/
	"git tag -a <tag_name> -m <descrip> <commitID>"
	
	"git tag" can show the list of tags
	"git show <tag_name>"
//tag operations
	"git tag -d <tag_name>"
if tag has been push to remote_repo, then:
	1,"git tag -d <tag_name>"
	2,"git push <remote_repo_name> :refs/tags/<tag_name>"
	"git push <remote_repo_name> <tag_name>"
	"git push <remote_repo_name> --tags"

//.gitignore
	"git check-ignore -v <file_full_name>"

//alias
	"git config --global alias.<tem_name> 'operate_name'"

//build a GIT server
1,	
	"sudo apt-get install git"
2,
	"sudo adduser git"
3,import id_rsa_pub to /home/git/.ssh/authorized_keys (one line for a key)
4,
	"sudo git init --bare sample.git"
	"sudo chown -R git:git sample.git"
5,forbid shell login: edit:/etc/passwd, change "git:x:1001:1001:,,,:/home/git:/bin/bash" into "git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell"
6,
	"git clone git@server:/srv/sample.git"
7,Gitosis: manage the SSH keys
8,Gitolite: manage the authorization
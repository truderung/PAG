

text_0 = "Was ist das nur für ein Durcheinander, bemerkte ich ..."


text_1 = """

put uncommitted changes to new branch

git status                               <-- review/list uncommitted changes
git stash                                <-- stash uncommitted changes
git stash branch <new-branch> stash@{1}  <-- create a branch from stash
git add .                                <-- add local changes
git status                               <-- review the status; ready to commit
git commit -m "local changes ..."        <-- commit the changes
git branch --list                        <-- see list of branches incl the one created above
git status                               <-- nothing to commit, working tree (new-branch) is clean
git checkout <old-branch>                <-- switch back


"""
# testing

Squash commits
```git rebase -i HEAD~3```

Rebase and squash (in current working branch)
```git rebase -i master```

If branch if ahead of master (no commits in master since branching)
```git merge <branch>```
fastforwards. All the commits of branch will be part of the master.

Squash and merge
```git merge --squash <branch>```
```git add . ```
```git commit -m <message>```
```git push```

If there are changes in master after branching
```git merge <branch>```
creates a single merge commit.

If there are no commits in master after branching but you want a single merge commit (no ff):
```git merge --no-ff <branch>```

Rewrite history and remove any stuff locally
```git reset --hard HEAD~1```
```git push -f```

Rewrite history but keep local changes (already added)
```git reset --soft HEAD~1```
```git push -f```

Rewrite history but keep local changes (not added)
```git reset --mixed HEAD~1```
```git push -f```

Rewrite commit message
```git commit --amend```
or ```git commit --amend -m "an updated commit message"```
```git push -f```

Forgot to commit stuff? Amend latest commit.
```git add hello.py```
```git commit ```
Realize you forgot to add the changes from main.py 
```git add main.py ```
```git commit --amend --no-edit```
Flag ```no-edit``` means keep the old commit message...


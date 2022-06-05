# testing

Squash commits
```git rebase -i HEAD~3```

Rebase and squash (in current working branch)
```git rebase -i master```

If branch if ahead of master (no commits in master)
```git merge <branch>```
fastforwards. All the commits of branch will be part of the master.

If you don't want all the commits to be part of master
```git merge --no-ff <branch>```

stuff!
other stuff!
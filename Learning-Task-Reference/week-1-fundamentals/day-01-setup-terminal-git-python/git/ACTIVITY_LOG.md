About Git:
-> Git is the distributed version control system that tracks changes to code over time.
-> It allows multiple developers to safely experiment, save snapshots of their progress &
-> Merge their work together without overwriting each other's files

The Flow of git:
-> Write the code or modify files on our computer.
-> Select the specified modified files to group together for your next saved snapshot.
-> Git permanently saved the snapshots to local project history.
-> Upload the local history to shared services like Github.

Why Git?
-> With git, we can maintain a reliable history of a project and coordinate team collaboration. 
-> Without Git, you would have to manually save duplicate folders to keep backups. 
Eg:
-> If two people edited the same file on a shared drive without version control, one person's save would immediately overwrite and destroy the other person's work.

How did you know it's working?
-> Check the local state by running git status, which will accurately list which files are changed, staged, or untracked.
-> verify your saved history by running git log to see your timeline of commits.
-> By running git push, we can see remote sync worked and successfully see it in the github.


Commands executed during task:

1. git status

C:\Users\Orcon\Downloads\Learning-Task-Reference>git status
On branch day-01-setup-terminal-git-python
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Learning-Task-Reference/week-1-fundamentals/day-01-setup-terminal-git-python/git/ACTIVITY_LOG.md

nothing added to commit but untracked files present (use "git add" to track)

-> Created the file called activity_log.md but currently it is in untracked status.

2. git branch

C:\Users\Orcon\Downloads\Learning-Task-Reference>git branch
* day-01-setup-terminal-git-python
  main

-> Recently, i'm using the day-01-setup-terminal-git-python branch which re-presented in *.

3. git switch

C:\Users\Orcon\Downloads\Learning-Task-Reference>git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

-> Previously, i was in day-01-setup-terminal-git-python branch, using switch command moved to main branch.

4. git add

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git add ACTIVITY_LOG.md

-> Once git add ran, file which goes to untracked to tracked file and in the local project history.

5. git commit

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git commit -m "About git & commands executed"
[day-01-setup-terminal-git-python cd8ca59] About git & commands executed
 1 file changed, 53 insertions(+)
 create mode 100644 Learning-Task-Reference/week-1-fundamentals/day-01-setup-terminal-git-python/git/ACTIVITY_LOG.md

 -> Commit means freeze the code for specific time which means permanent snapshot of our project at a specific time.

 6. git push

 C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git push origin day-01-setup-terminal-git-python
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.53 KiB | 1.53 MiB/s, done.
Total 7 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for 'day-01-setup-terminal-git-python' on GitHub by visiting:
remote:      https://github.com/saravananmohanraj/Learning-Task/pull/new/day-01-setup-terminal-git-python
remote:
To https://github.com/saravananmohanraj/Learning-Task.git
 * [new branch]      day-01-setup-terminal-git-python -> day-01-setup-terminal-git-python

 -> Once add and commit it, using push command to share the code to the github.

 7. git pull

-> If the changes occured in the main branch we need to get that changes into our local branch.
-> We can use the pull command to merge it.

8. git fetch

-> We can get the changed code from the remote branch repostories but don't get merged into local branch.

9. .gitignore

C:\Users\Orcon\Downloads\Learning-Task-Reference>echo "__pycache__/" > .gitignore

C:\Users\Orcon\Downloads\Learning-Task-Reference>echo ".venv/" >> .gitignore

C:\Users\Orcon\Downloads\Learning-Task-Reference>git add .gitignore

C:\Users\Orcon\Downloads\Learning-Task-Reference>git commit -m "Add .gitignore to exclude cache and venv"
[day-01-setup-terminal-git-python d304db0] Add .gitignore to exclude cache and venv
 1 file changed, 2 insertions(+)
 create mode 100644 .gitignore

 -> Hidden configuration file and added Cconfiguration file and added __pycache__/ to block Python's temporary compiled bytecode from being tracked.
 -> Appended .venv/ to block your local virtual environment, which contains thousands of packages specific only to our computer.
 -> Permanently saved these exclusion rules into the project's history so they apply to everyone.

10. git merge

C:\Users\Orcon\Downloads\Learning-Task-Reference>git switch branch-1
Switched to branch 'branch-1'

C:\Users\Orcon\Downloads\Learning-Task-Reference>echo "Second update" >> test.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference>git commit -am "Second update to base"
[branch-1 3c72cfb] Second update to base
 1 file changed, 1 insertion(+)

C:\Users\Orcon\Downloads\Learning-Task-Reference>git switch test-merge
Switched to branch 'test-merge'

C:\Users\Orcon\Downloads\Learning-Task-Reference>git merge branch-1
Merge made by the 'ort' strategy.
 test.txt | 1 +
 1 file changed, 1 insertion(+)

Merge branch 'branch-1' into test-merge
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
~                                                                                                                    ~                                                                                                                       ~                                                                                                                                 .git/MERGE_MSG [unix] (21:53 04/11/2026)                                                                         
1,1 All"~/Downloads/Learning-Task-Reference/.git/MERGE_MSG" [unix] 6L, 266B

-> combine the branches ( of branch-1 into test-merge ) and create a new merge commit, preserving the split history.

11. git rebase

C:\Users\Orcon\Downloads\Learning-Task-Reference>git switch test-rebase
Already on 'test-rebase'

C:\Users\Orcon\Downloads\Learning-Task-Reference>echo "Rebase work" > rebase.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference>git add rebase.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference>git commit -m "My rebase work"
[test-rebase 0970edb] My rebase work
 1 file changed, 1 insertion(+)
 create mode 100644 rebase.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference>git rebase branch-1
Successfully rebased and updated refs/heads/test-rebase.

-> rewrite the history by moving your new work to the very tip of the updated base, creating a straight line.

12. git restore

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>echo "Mistake" > undo-test.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git add undo-test.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git commit -m "for restore command to run"
[test-merge 9db63d4] for restore command to run
 1 file changed, 1 insertion(+)
 create mode 100644 Learning-Task-Reference/week-1-fundamentals/day-01-setup-terminal-git-python/git/undo-test.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>echo "A terrible mistake" >> undo-test.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>type undo-test.txt
"Mistake"
"A terrible mistake"

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git restore undo-test.txt
"Mistake"

-> Uncommitted changes will revert to normal with tracked commits.

13. git reset soft

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git reset --soft HEAD~1

-> undo the commits, but keep the file.

14. git reset hard

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git reset --hard HEAD~2
HEAD is now at 73f80f7 Base commit

-> Destroy our .gitignore and delete the file

15. git revert

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>echo "Bad idea" > bad-file.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git add bad-file.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git commit -m "Bad commit"
[test-merge cc3d18c] Bad commit
 1 file changed, 1 insertion(+)
 create mode 100644 Learning-Task-Reference/week-1-fundamentals/day-01-setup-terminal-git-python/git/bad-file.txt

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\git>git revert HEAD --no-edit
[test-merge 7a5678a] Revert "Bad commit"
 Date: Wed Nov 4 22:40:09 2026 +0530
 1 file changed, 1 deletion(-)
 delete mode 100644 Learning-Task-Reference/week-1-fundamentals/day-01-setup-terminal-git-python/git/bad-file.txt 

-> Safely creates a new commit that deletes bad-file.txt 

16. git log

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference>git log
commit ba2dbe8f9953f8960a00fcf2d1b78dc813e866d8 (HEAD -> day-01-setup-terminal-git-python)
Author: Saravanan Srikanth <saravanan@saturam.com>
Date:   Wed Nov 4 22:46:49 2026 +0530

    Recreate .gitignore after hard reset

commit 898c5c430a81b2582adc09d82ac453ce48542eea (origin/day-01-setup-terminal-git-python)
Author: Saravanan Srikanth <saravanan@saturam.com>
Date:   Wed Nov 4 22:18:06 2026 +0530

    Added .gitignore configuration file

commit d304db05c0e4c2f385518317866806986d537b90
Author: Saravanan Srikanth <saravanan@saturam.com>
Date:   Wed Nov 4 22:12:38 2026 +0530

    Add .gitignore to exclude cache and venv

commit 03ffead2059512a46757a89d00759eb56269a107
Author: Saravanan Srikanth <saravanan@saturam.com>
Date:   Wed Nov 4 13:24:18 2026 +0530

    git commands executed part-1

commit cd8ca590ff75253f82e3c7390a528c7bebbcecd3
Author: Saravanan Srikanth <saravanan@saturam.com>
Date:   Wed Nov 4 13:05:48 2026 +0530

    About git & commands executed
 ^X
commit ba2dbe8f9953f8960a00fcf2d1b78dc813e866d8 (HEAD -> day-01-setup-terminal-git-python)
Author: Saravanan Srikanth <saravanan@saturam.com>
Date:   Wed Nov 4 22:46:49 2026 +0530

-> It will give the commit logs.

17. git log --online

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference>git log --graph
* commit ba2dbe8f9953f8960a00fcf2d1b78dc813e866d8 (HEAD -> day-01-setup-terminal-git-python)
| Author: Saravanan Srikanth <saravanan@saturam.com>
| Date:   Wed Nov 4 22:46:49 2026 +0530
|
|     Recreate .gitignore after hard reset
|
* commit 898c5c430a81b2582adc09d82ac453ce48542eea (origin/day-01-setup-terminal-git-python)
| Author: Saravanan Srikanth <saravanan@saturam.com>
| Date:   Wed Nov 4 22:18:06 2026 +0530
|
|     Added .gitignore configuration file
|
* commit d304db05c0e4c2f385518317866806986d537b90
| Author: Saravanan Srikanth <saravanan@saturam.com>
| Date:   Wed Nov 4 22:12:38 2026 +0530
|
|     Add .gitignore to exclude cache and venv
|
* commit 03ffead2059512a46757a89d00759eb56269a107
| Author: Saravanan Srikanth <saravanan@saturam.com>
| Date:   Wed Nov 4 13:24:18 2026 +0530
|
|     git commands executed part-1
|
* commit cd8ca590ff75253f82e3c7390a528c7bebbcecd3
| Author: Saravanan Srikanth <saravanan@saturam.com>
| Date:   Wed Nov 4 13:05:48 2026 +0530
|
|     About git & commands executed

-> It shows standard history with extra timeline in the left corner.

18. git log --oneline --graph

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference>git log --oneline --graph
* ba2dbe8 (HEAD -> day-01-setup-terminal-git-python) Recreate .gitignore after hard reset
* 898c5c4 (origin/day-01-setup-terminal-git-python) Added .gitignore configuration file
* d304db0 Add .gitignore to exclude cache and venv
* 03ffead git commands executed part-1
* cd8ca59 About git & commands executed
* c311d29 (origin/main, origin/HEAD, main) Initial commit of repo

-> Compresses the history and shrinks long commit ID to 7 characters, easy-to-read.
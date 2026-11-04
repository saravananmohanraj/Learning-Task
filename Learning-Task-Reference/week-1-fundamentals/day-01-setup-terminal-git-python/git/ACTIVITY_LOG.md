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

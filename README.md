# LR6
Лабораторная работа №6

dstepanchenko@WC-NB-178 MINGW64 ~/Documents/ГУАП/LR6_v1 (master)
$ git fetch https://github.com/mojik88/LR6_v1.git
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 1.76 KiB | 64.00 KiB/s, done.
From https://github.com/mojik88/LR6_v1
 * branch            HEAD       -> FETCH_HEAD

dstepanchenko@WC-NB-178 MINGW64 ~/Documents/ГУАП/LR6_v1 (master)
$ git fetch https://github.com/mojik88/LR6_v1.git
From https://github.com/mojik88/LR6_v1
 * branch            HEAD       -> FETCH_HEAD

dstepanchenko@WC-NB-178 MINGW64 ~/Documents/ГУАП/LR6_v1 (master)
$ git pull https://github.com/mojik88/LR6_v1.git
From https://github.com/mojik88/LR6_v1
 * branch            HEAD       -> FETCH_HEAD
Updating 921f53b..d4540f9
Fast-forward
 Task1.txt | 2 ++
 1 file changed, 2 insertions(+)
commit f5702c34f432613bd8a20b1a6c270d774dab878e
Author: mojik88 <mojik88@gmail.com>
Date:   Wed Nov 13 14:57:59 2024 +0300

    Create Task1

commit 921f53b8d0cebf542c791cf31f04e9b792f385a4 (origin/master, origin/HEAD)
Author: Kurtyanik <45309985+Kurtyanik@users.noreply.github.com>
Date:   Sat Nov 21 20:09:49 2020 +0300

    Обновление информации

commit c08a654a63cfc3a7146b2b7015884d9020f5cbf5
Author: Kurtyanik <45309985+Kurtyanik@users.noreply.github.com>
Date:   Sat Nov 21 20:02:16 2020 +0300

    Файл создан пустым

commit 3c6e9131bb47ed6009c28226afb0535c7f6d5964
Author: Kurtyanik <45309985+Kurtyanik@users.noreply.github.com>
Date:   Sat Nov 21 19:58:20 2020 +0300


dstepanchenko@WC-NB-178 MINGW64 ~/Documents/ГУАП/LR6_v1 (report-branch)
$ git log -p -1
commit 4c735a6905f468b1ccb26f98e37cc317411d0df3 (HEAD -> report-branch, master)
Author: Denis Stepanchenko B3441 <dstepanchenko@westconcept.ru>
Date:   Wed Nov 13 15:10:57 2024 +0300

    Revert "Rename Task1 to Task1.txt"

    This reverts commit d4540f91bd8cfb3e3569bc60c8d3b873e51defcf.

diff --git a/Task1.txt b/Task1
similarity index 100%
rename from Task1.txt
rename to Task1




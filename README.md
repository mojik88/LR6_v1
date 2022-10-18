Лабораторная работа №6.
Выполнил: Николаев Дмитрий Сергеевич 4117.
Создан аккаунт на сайте GitHub, а также сделана копия в личное хранилище из https://github.com/Kurtyanik/LR6/ (Fork).
![][screen/screen1]
Установлен Git и  настроен клиент git, введя имя пользователя (Группа
Фамилия И.О.) и email. 
![][screen/screen2]
Клонирован свой личный удалённый репозиторий на компьютер. 
![][screen/screen3]
Добавлен файл через интерфейс GitHub. Подтянуты изменения в
локальный репозиторий
![][screen/screen4]
Получина историю операций для каждой из веток. 
Ветка master
![][screen/screen5]
Ветка branch1
![][screen/screen6]
Выполнено слияние в ветку master.
![][screen/screen7]
Конфликт разрешен, с помощью mergetool vimdiff.
![][screen/screen8]
![][screen/screen9]
Итоговый результат сохранен и записан commit.
![][screen/screen10]
Удалена побочная ветка после успешного слияния.
![][screen/screen11]
Сделаны и зафиксированы изменения.
![][screen/screen12]
![][screen/screen13]
Зафиксирован лог изменений.
![][screen/screen14]
Сделан откат коммита.
![][screen/screen15]
Создана ветка отчёта.
![][screen/screen16]
Заполнение отчета в среде Brackets.
![][screen/screen17]
Получена история операций в форматированном виде (сокращённый
хэш + дата + имя автора + комментарий).
![][screen/screen18]


Лог команд
$ cd Desktop/TestGit/
$ git clone https://github.com/TanukiY/LR6
$ cd LR6/
$ git pull
$ git log
$ git checkout branch1
$ git branch
$ git merge branch1
$ git mergetool
$ git status
$ git add .
$ git commit -m "Merge"
$ git branch -d branch1
$ git commit -m "Add index.html"
$ git commit -m "Add ABS.txt"
$ git reset --hard HEAD~1
$ git checkout -b otchet




#Лабораторная работа №6.
> Выполнил: Николаев Дмитрий Сергеевич 4117.
Создан аккаунт на сайте GitHub, а также сделана копия в личное хранилище из https://github.com/Kurtyanik/LR6/ (Fork).
![][screen/screen1.png]
Установлен Git и  настроен клиент git, введя имя пользователя (Группа
Фамилия И.О.) и email. 
![][screen/screen2.png]
Клонирован свой личный удалённый репозиторий на компьютер. 
![][screen/screen3.png]
Добавлен файл через интерфейс GitHub. Подтянуты изменения в
локальный репозиторий
![][screen/screen4.png]
Получина историю операций для каждой из веток. 
Ветка master
![][screen/screen5.png]
Ветка branch1
![][screen/screen6.png]
Выполнено слияние в ветку master.
![][screen/screen7.png]
Конфликт разрешен, с помощью mergetool vimdiff.
![][screen/screen8.png]
![][screen/screen9.png]
Итоговый результат сохранен и записан commit.
![][screen/screen10.png]
Удалена побочная ветка после успешного слияния.
![][screen/screen11.png]
Сделаны и зафиксированы изменения.
![][screen/screen12.png]
![][screen/screen13.png]
Зафиксирован лог изменений.
![][screen/screen14.png]
Сделан откат коммита.
![][screen/screen15.png]
Создана ветка отчёта.
![][screen/screen16.png]
Заполнение отчета в среде Brackets.
![][screen/screen17.png]
Получена история операций в форматированном виде (сокращённый
хэш + дата + имя автора + комментарий).
![][screen/screen18.png]


Лог команд
```
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
```



### Лабораторная работа №6.
> Выполнил: Николаев Дмитрий Сергеевич 4117.
***

Создан аккаунт на сайте GitHub, а также сделана копия в личное хранилище из https://github.com/Kurtyanik/LR6/ (Fork).

![This is an image][Screen/screen1.png]

Установлен Git и  настроен клиент git, введя имя пользователя (Группа
Фамилия И.О.) и email. 
![This is an image][Screen/screen2.png]
Клонирован свой личный удалённый репозиторий на компьютер. 
![This is an image][Screen/screen3.png]
Добавлен файл через интерфейс GitHub. Подтянуты изменения в
локальный репозиторий
![This is an image][Screen/screen4.png]
Получина историю операций для каждой из веток. 
Ветка master
![This is an image][Screen/screen5.png]
Ветка branch1
![This is an image][Screen/screen6.png]
Выполнено слияние в ветку master.
![This is an image][Screen/screen7.png]
Конфликт разрешен, с помощью mergetool vimdiff.
![This is an image][Screen/screen8.png]
![This is an image][Screen/screen9.png]
Итоговый результат сохранен и записан commit.
![This is an image][Screen/screen10.png]
Удалена побочная ветка после успешного слияния.
![This is an image][Screen/screen11.png]
Сделаны и зафиксированы изменения.
![This is an image][Screen/screen12.png]
![This is an image][Screen/screen13.png]
Зафиксирован лог изменений.
![This is an image][Screen/screen14.png]
Сделан откат коммита.
![This is an image][Screen/screen15.png]
Создана ветка отчёта.
![This is an image][Screen/screen16.png]
Заполнение отчета в среде Brackets.
![This is an image][Screen/screen17.png]
Получена история операций в форматированном виде (сокращённый
хэш + дата + имя автора + комментарий).
![This is an image][Screen/screen18.png]
***


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



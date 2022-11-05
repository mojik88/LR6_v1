# LR6
Лабораторная работа №6


+ Просмотр истории операций и последних трёх изменений ветки branch1 (git log и git log -p-3)

 ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/9.png)
 ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/10.png)

+ Слияние двух веток в одну (переходим в ветку master (git checkout <ветка>) и производим слияние веток (git merge branch1))
Переход на ветку master нужен т.к. по заданию необходимо получить слияние в ветку master


  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/11.png)

+ Анализ состояния проекта с использованием git status. 
**Ошибка:** лияние не происходит т.к. есть "несоединённая часть". 
Разрешение конфликта (git add <file>)

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/12.png)

+ Проверка готовности к дальнейшему слиянию с помощью команды git status. Конфликты разрешены.

Для завершения процесса необходимо прописать команду git commit -m

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/13.png)

+ Удаление побочной ветки после слияния с помощью git branch -d <ветка>

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/14.png)

+ Проверка правильности выполнения с помощью git branch

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/15.png)


+ Создание изменений (созданы 2 текстовых файла), используемые команды:

echo текст_изменения > файл_для_сохранения
git add <файл>
git commit -m "изменение n"

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/16.png)


  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/17.png)



+ История операций (git log -3)

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/18.png)



+ Откат коммита (git reset HEAD~1) и проверка с помощью истории изменений (git log)

  ![](https://github.com/barbolin-semyon/LR6/blob/master/screens/19.png)

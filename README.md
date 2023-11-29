# LR6
Лабораторная работа №6

***Цель рабораторной работы:*** *изучение базовых возможностей системы управления версиями, опыт работы с Git Api, опыт работы с локальным удаленным репозиторием.*

Выполнение работы:

- Сделать Fork репозитория в личное хранилище GitHub:
- Клонировать свой личный удалённый репозиторий на компьютер:
```
git clone https://github.com/kedaea/LR6.git
```
- Добавить файл через интерфейс GitHub. Подтянуть изменения в локальный репозиторий:
```
git pull
```
- Получить историю операций для каждой из веток:
```
git log --graph
```
- Посмотреть последние изменения:
```
git log
```
- Выполнить слияние в ветку master, разрешив конфликт:
```
git chekout -b new_branch
git add .
git commit -m "file change in new_branch"
git add .
git commit -m "file change in new_branch"
git chekout master
git merge new_branch
```
- Удалить побочную ветку после успешного слияния:
```
git branch -d new_branch
```
- Сделать изменения и зафиксировать их, оставляя комментарии, несколько раз:
```
git add .
git commit -m "file after merging from master"
```
- Сделать откат коммита:
```
get reset --soft HEAD~1
git log
```
- Создать ветку для отчёта:
```
git checkout -b report
```
- Начать оформлять отчет.
- Получить историю операций в форматированном виде:
```
git log --pretty=format: "%h %ad %an %s"
```
- Отправить локальные изменения в сетевое хранилище GitHub:
```
get push -u origin
```

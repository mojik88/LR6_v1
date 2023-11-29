# LR6
Лабораторная работа №6

***Цель рабораторной работы:*** *изучение базовых возможностей системы управления версиями, опыт работы с Git Api, опыт работы с локальным удаленным репозиторием.*

Выполнение работы:

- Сделать Fork репозитория в личное хранилище GitHub:
![screen01](https://github.com/kedaea/LR6/blob/master/screenshots/1.png)
- Клонировать свой личный удалённый репозиторий на компьютер:
![screen02](https://github.com/kedaea/LR6/blob/master/screenshots/2.png)
```
git clone https://github.com/kedaea/LR6.git
```
- Добавить файл через интерфейс GitHub. Подтянуть изменения в локальный репозиторий:
![screen03](https://github.com/kedaea/LR6/blob/master/screenshots/3.png)
```
git pull
```
- Получить историю операций для каждой из веток:
![screen04](https://github.com/kedaea/LR6/blob/master/screenshots/4.png)
```
git log --graph
```
- Посмотреть последние изменения:
![screen05](https://github.com/kedaea/LR6/blob/master/screenshots/5.png)
```
git log
```
- Выполнить слияние в ветку master, разрешив конфликт:
![screen06](https://github.com/kedaea/LR6/blob/master/screenshots/6.png)
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
![screen07](https://github.com/kedaea/LR6/blob/master/screenshots/7.png)
```
git branch -d new_branch
```
- Сделать изменения и зафиксировать их, оставляя комментарии, несколько раз:
![screen08](https://github.com/kedaea/LR6/blob/master/screenshots/8.png)
```
git add .
git commit -m "file after merging from master"
```
- Сделать откат коммита:
![screen09](https://github.com/kedaea/LR6/blob/master/screenshots/9.png)
```
get reset --soft HEAD~1
git log
```
- Создать ветку для отчёта:
![screen10](https://github.com/kedaea/LR6/blob/master/screenshots/10.png)
```
git checkout -b report
```
- Начать оформлять отчет.
- Получить историю операций в форматированном виде:
![screen11](https://github.com/kedaea/LR6/blob/master/screenshots/11.png)
```
git log --pretty=format: "%h %ad %an %s"
```
- Отправить локальные изменения в сетевое хранилище GitHub:
```
git push -u origin
```

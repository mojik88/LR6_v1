# LR6

Лабораторная работа №6

Создаем копию репозитория в личное хранилище.

Настраиваем клиент git. Вводим свое пользовательское имя и почту с помощью команд git config --global user.name <username>; git config --global user.email <email>.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image1.jpg)

Клонируем удаленный репозиторий на компьютер командой git clone <url>.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image2.jpg)

Добавляем файл через интерфейс GitHub. Подтягиваем изменения в локальный репозиторий командой git pull.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image3.jpg)

Для просмотра коммитов ветки master используем команду git log.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image4.jpg)

Смотрим существующие ветки с помощью команды git branch. Переходим в ветку branch1 командой git checkout branch1.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image5.jpg)

Теперь посмотрим коммиты ветки branch1 командой git log.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image6.jpg)

Для подробного рассмотрения используем команду  git log -p.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image7.jpg)

Слияние в ветку master происходит с помощью команды git merge branch1.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image8.jpg)

Возникает конфликт из-за того, что он был незакоммичен и изменен. Используем команду get status  чтобы узнать это. Решаем конфликт с помощью команды git add mergefile.txt; git commit -m "Branches".

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image9.jpg)

После слияния удаляем побочную ветку командой git branch -d branch1.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image10.jpg)

Создаем изменения в новом файле с помощью команд git add .; git status; git commit.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image11.jpg)

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image12.jpg)

"Хард" откат коммита делаем с помощью команды git reset --hard HEAD~1.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image13.jpg)

Создаем ветку для отчета командой git chekout -b 'reportKurchugina'.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image14.jpg)

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image15.jpg)

Отчет пишем в файле README.md.

Итоговую историю операций получаем с помощью команды git log.

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image16.jpg)

![Image alt](https://github.com/linakpo/LR6/raw/reportKurchugina/Screenshots/image17.jpg)

Отчет необходимо сохранить и выполнить команды git add и git commit.

В конце необходимо отправить все локальные изменения командой git push.
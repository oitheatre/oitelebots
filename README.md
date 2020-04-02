Это небольшой фреймворк для создания ботов в структуру Ой Театра.
Внутри используется [Flask](https://flask.palletsprojects.com/) (микрофреймворк для веба) и [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (тг обёртка).

Каждый бот представляет из себя минисервис, который крутится на нашем сервере telegram.oitheatre.ru

# Quick start

Если вы хотите поковыряться в каком-нибудь боте, что-нибудь подправить:

0. Получить секретный ключ от сервера у Влада Т.
1. `edit ~/.ssh/config # или как еще можете настройте на своей системе гит, чтобы он использовал этот ключ`
2. `git clone git@github.com:oitheatre/oitelebots.git`
3. `cd oitelebots`
4. `scp -i /path/to/private.key tgbot@telegram.oitheatre.ru:./oitelebots/{cert.pem,private.key,bot_settings.yml} .`
5. `python -m venv venv # if you would like`
6. `source venv/bin/activate`
7. `pip install -r requirements.txt`
8. `git checkout yourbotname # переключитесь на ветку нужного бота`
8. `ssh -i /path/to/private.key -R 8444:127.0.0.1:8443 -N tgbot@telegram.oitheatre.ru # пробрасываем нужные порты, здесь это 8444 для oitestbot (8443 + NUMBER_ID. NUMBER_ID смотри в bot_settings.yml)`
9. `BOT_NAME=yourbotname flask run`
10. После работы хорошо бы снова установить вебхук на PRODUCTON порт сервера, чтобы обновления приходили боту на сервере. Самый простой способ это сделать запустить `FLASK_ENV=production BOT_NAME=yourbotname flask run`. Скорее всего ваше приложение упадет, так как будет требовать прав рута для 88 порта. Но нам это и неважно, так как вебхук уже будет переустановлен. Проверьте, что бот действительно откликается и работает


# Добавление нового бота

Если вы захотели создать нового бота и развернуть его на сервере:

0. Зарегистрировать бота и получить свой токен. Пишем в телеграмме боту @BotFather
1. `ssh -A -i /path/to/private.key tgbot@telegram.oitheatre.ru # вам нужно настроить форвард вашего ключа, чтобы использовать на сервере гит`
2. `cd oitelebots`
3. `git branch && git status# проверьте на всякий случай, что вы на мастере и на сервере не лежит никакого мусора`
4. `cp -r app/oitestbot app/yourbotname`
5. `edit app/yourbotname/* # заменить все вхождения oitestbot на yourbotname; замени текст в bot.py def start(), чтобы отличать своего бота`
6. `edit bot_settings.yml # добавляем секцию для своего бота по примеру oitestbot`
7. `edit docker-compose.yml # добавляем бот в docker-compose по примеру oitestbot`
8. `docker-compose up -d --build bot_name # запускаем бота-заглушку`
9. `python3 ./new_bot_nginx.py > nginx/telegram.conf # генерируем конфиг для nginx`
10. `docker exec nginx-tgbots nginx -s reload # перезагружаем nginx с нашими настройками`
11. `git add & git commit -m 'add yourbotname' && git push # если все хорошо`
12. Напишите вашему боту в тг команду /start, проверьте что он действительно работает и высылает вам текст, который вы прописали в пункте 5

Теперь небольшая цепочка действий на своей локальной машине:
1. `git checkout master && git status`
2. `git pull -u origin master`
3. `git checkout -b yourbotname # пожалуйста, плиз, создайте для вашего бота ветку, не работайте в мастере`
4. Работаем локально на своей машине. Как это делать - описано разделом выше
5. `git push -u origin yourbotname # пусть ваша ветка уйдет на гитхаб, чтобы другие могли пользоваться`

# Внесение изменений бота в мастер

Вы большой молодец, проделали работу, получили функционального бота и теперь хотите, чтобы он постоянно крутился на вашем сервере. Для этого делаем локально:
1. `git merge master && git checkout master && git merge yourbranch && git push # локально мержим все ваше добро в мастер`
2. `ssh -A -i /path/to/private.key tgbot@telegram.oitheatre.ru # идем на сервер, вам нужно настроить форвард вашего ключа, чтобы использовать на сервере гит`
3. `git checkout master && git status`
4. `git pull`
5. `docker-compose up -d --build yourbotname # билдим снова нашего бота`

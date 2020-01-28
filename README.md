Это небольшой фреймворк для создания ботов в структуру Ой Театра.
Внутри используется [Flask](https://flask.palletsprojects.com/) (микрофреймворк для веба) и [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (тг обёртка).

Каждый бот представляет из себя минисервис, который крутится на нашем сервере telegram.oitheatre.ru

# Quick start

Если вы хотите поковыряться в каком-нибудь боте, что-нибудь подправить:

0. Получить секретный ключ от сервера у Влада Т.
1. edit ~/.ssh/config # или как еще можете настройте на своей системе гит, чтобы он использовал этот ключ
2. git clone git@github.com:oitheatre/oitelebots.git
3. cd oitelebots
4. scp -i /path/to/private.key tgbot@telegram.oitheatre.ru:./oitelebots/{cert.pem,private.key,bot_settings.yml} .
5. python -m venv venv # if you would like
6. source venv/bin/activate
7. `pip install -r requirements.txt`
8. ssh -i /path/to/private.key -R 8444:127.0.0.1:8443 -N tgbot@telegram.oitheatre.ru # пробрасываем нужные порты, здесь это 8444 для oitestbot (8443 + NUMBER_ID)
9. BOT_NAME=oitestbot flask run # заменить oitestbot на имя своего бота


# Добавление нового бота

Если вы захотели создать нового бота и развернуть его на сервере:

0. Зарегистрировать бота и получить свой токен. Пишем в телеграмме боту @BotFather
1. ssh -A -i /path/to/private.key tgbot@telegram.oitheatre.ru # вам нужно настроить форвард вашего ключа, чтобы использовать на сервере гит
2. cd oitelebots
3. git checkout -b your_branch # создадим свою ветку и сделаем заглушку бота
4. cp -r app/oitestbot app/yourbotname
5. edit app/yourbotname/* # заменить все вхождения oitestbot на yourbotname
6. edit bot_settings.yml # добавляем секцию для своего бота по примеру oitestbot
7. edit docker-compose.yml # добавляем бот в docker-compose по примеру oitestbot
8. docker-compose up -d --build bot_name # запускаем бота-заглушку
9. ./new_bot_nginx.py > nginx/telegram.conf # генерируем конфиг для nginx
10. docker exec nginx-tgbots nginx -s reload # перезагружаем nginx с нашими настройками
11. git add & git commit $ git push -u origin yourbranch # если все хорошо
12. Теперь обновите репу на своей локальной машине, переключитесь на только что созданную ветку и можете запускать вашего бота как в разделе выше (scp, ssh -R порты, BOT_NAME flask run)

# oitelebots


Если вы хотите поковыряться в каком-нибудь боте, что-нибудь подправить:
0. Получить секретный ключ от сервера у Влада Т.
1. git clone git@github.com:oitheatre/oitelebots.git
2. cd oitelebots
3. scp tgbot@telegram.oitheatre.ru:./oitelebots/{cert.pem,private.key,bot_settings.yml} .
4. python -m venv venv # if you would like
5. source venv/bin/activate
6. pip install -r requirements.txt
7. ssh -R 8444:127.0.0.1:8443 -N tgbot@telegram.oitheatre.ru # пробрасываем нужные порты, здесь это 8444 (8443 + NUMBER_ID)
8. BOT_NAME=yourbotname flask run

Если вы захотели создать нового бота и развернуть его на сервере:
0. Зарегистрировать бота и получить свой токен. Пишем в телеграмме боту @BotFather
1. ssh tgbot@telegram.oitheatre.ru
2. cd oitelebots
3. Создать новую ветку и сделать заглушку для нового бота?
4. nano bot_settings.yml # добавляем секцию для своего бота по примеру oitestbot
5. nano docker-compose.yml # добавляем бот в docker-compose по примеру oitestbot
6. docker-compose up -d --build bot_name # запускаем бота-заглушку
7. ./new_bot_nginx.py > nginx/telegram.conf # генерируем конфиг для nginx
8. docker exec nginx-tgbots nginx -s reload # перезагружаем nginx с нашими настройками

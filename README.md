# oitelebots

ssh -R 8444:127.0.0.1:8443 -N sshoi

Если вы хотите принять участие в разработке:
0. Получить секретный ключ от сервера у Влада Т.
1. git clone git@github.com:oitheatre/oitelebots.git
2. cd oitelebots
3. scp tgbot@telegram.oitheatre.ru:./oitelebots/{cert.pem,private.key,bot_settings.yml} .
4. python -m venv venv # if you would like
5. source venv/bin/activate
6. pip install -r requirements.txt
7. flask run

Если вы захотели создать и запустить свой бот, то вам нужно сделать следующие шаги:
0. Зарегистрировать бота и получить свой токен. Пишем в телеграмме боту @BotFather
1. ssh sshoi
2. cd oitelebots
3. Добавляем в bot_settings.yml секцию для своего бота


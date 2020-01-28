# export FLASK_SKIP_DOTENV=1
FROM python:3.7-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/local/bin/flask", "run", "-h", "0.0.0.0"]

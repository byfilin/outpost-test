FROM python:3.10-alpine

ENV DOCKER_APP True

RUN apk update
RUN apk add git

RUN git config --global user.email "you@example.com"
RUN git config --global user.name "Your Name"

WORKDIR /app

ENTRYPOINT ["python3", "nginx_parser.py", "nginx.log", "result.csv"]
# FROM python:3.10-alpine

# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8

# RUN mkdir /app
# COPY ./requirements.txt /app

# # Install required package
# RUN apk update && \
#     apk add --no-cache --virtual .build-deps \
#     ca-certificates gcc postgresql-dev linux-headers musl-dev \
#     libffi-dev jpeg-dev zlib-dev \
#     git bash

# # Install requirements.txt
# RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# COPY . /app
# WORKDIR /app

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000" ]

# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --update add bash && \
    apk add dos2unix

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
RUN mkdir -p /usr/src/app/
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN dos2unix ./entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
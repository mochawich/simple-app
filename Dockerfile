FROM python:2.7

ARG APP_ENV=training

# Define the working directory and copy the app files to it
RUN mkdir /simple-app
WORKDIR /simple-app
ADD . /simple-app/

# Install the app requirements
RUN pip install -r src/requirements.txt

EXPOSE 8001

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8
ENV APP_ENV $APP_ENV

CMD newrelic-admin run-program gunicorn src.wsgi -c /api/src/settings_gunicorn.py

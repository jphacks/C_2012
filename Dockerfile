FROM python:3.6

RUN apt-get update -qq
RUN apt-get install -y libgl1-mesa-dev

# install heroku cli
RUN curl https://cli-assets.heroku.com/install.sh | sh

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt

RUN apt-get install -y poppler-utils

RUN pip install -r requirements.txt

ADD . /user/src/app
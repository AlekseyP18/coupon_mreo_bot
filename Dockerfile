FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim \
    && apt-get install -y postgresql-client build-essential libpq-dev

COPY requirements.txt /temp/
RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password --gecos "" user

COPY . /src
WORKDIR /src

RUN chown -R user:user .

USER user

CMD [ "python", "main.py" ]
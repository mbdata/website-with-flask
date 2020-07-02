FROM python:3.7.5-slim-buster

# create new folder 'website' and set it as workdir
ENV INSTALL_PATH /website
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:9000 --access-logfile - "website.app:create_app()"

FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN  apt-get update
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
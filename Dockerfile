FROM python:2.7

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY / /my_project/
FROM python:3.5.7-alpine3.9 

ADD . /
RUN pip3 install -r requirements.sh
CMD [ "python", "./main.py" ]


FROM python:3.6-alpine

COPY . /IronicBot
WORKDIR /IronicBot

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME Ironic_Bot

CMD ["python", "./Bot_Main.py"]

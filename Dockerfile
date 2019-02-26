FROM python:3.6

WORKDIR /app

RUN apt-get update
RUN apt-get install -y git
RUN pip install --upgrade setuptools

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "Bot_Main.py"]
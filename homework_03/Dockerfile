FROM python:3.9-buster

WORKDIR /homework_03

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD uvicorn app:app --host=0.0.0.0
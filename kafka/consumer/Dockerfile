FROM python:3.8
WORKDIR /code

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "kafka/consumer/kafka_consumer.py" ]
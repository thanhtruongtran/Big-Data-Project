import time
import os
import sys
sys.path.append(os.path.getcwd())
from utils.logger_utils import get_logger
from json import dumps, loads
from kafka import KafkaProducer


logger = get_logger("Kafka Producer")
time.sleep(30)

try:
    producer = KafkaProducer(bootstrap_servers=['kafka:29092'],
                          value_serializer=lambda x: 
                          dumps(x).encode('utf-8'))
except:
    logger.info("Kafka Producer not connected")

jsonFile = open("data/hb-data.json", "r+")
for line in jsonFile:
  jsonLine = loads(line)
  producer.send('hb', value=jsonLine)
  print(jsonLine)
  
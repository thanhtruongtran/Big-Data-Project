import time
import os
import sys
sys.path.append(os.path.getcwd())
import hdfs
from kafka import KafkaConsumer
from json import loads
from utils.logger_utils import get_logger


logger = get_logger("Kafka Consumer")
time.sleep(30)

try:
    consumer = KafkaConsumer(
        'hb',
        bootstrap_servers=['kafka:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
      )
except:
    logger.info("Kafka Consumer not connected")

for message in consumer:
    message = message.value
    hdfs.write_to_hdfs(str(message))
    print(message)
    
    
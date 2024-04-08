import json
import time 

from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

server = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=json_serializer
)

producer.bootstrap_connected()

t0 = time.time()

topic_name = 'test-topic'

for i in range(10):
    message = {'number': i}
    producer.send(topic_name, value=message)
    print(f"Sent: {message}")
    time.sleep(0.05)

t2 = time.time()

producer.flush()

t1 = time.time()
print(f'took {(t1 - t0):.2f} seconds')
print(f'Sending took {(t2 - t0):.5f} seconds')
print(f'Flushing took {(t1- t2):.5f} seconds')

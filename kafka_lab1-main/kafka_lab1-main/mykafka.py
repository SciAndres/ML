import csv
import time
from kafka import KafkaProducer
from json import dumps
from kafka import KafkaConsumer
from json import loads

def kafka_producer(csv_file_path, topic_name="kafka_ml1", limit=10, sleep_time=3):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

   
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        count = 0
        for row in csv_reader:
           
            producer.send(topic_name, value=row)
            print(f"Message sent: {row}")

            count += 1
            if count >= limit:
                break

           
            time.sleep(sleep_time)


csv_path = r'C:/Users/enrri/OneDrive/Documentos/Universidad/Semestre 4/ETL/datos.csv'
kafka_producer(csv_path, topic_name="kafka_ml1", limit=10, sleep_time=3)




def kafka_consumer(topic_name="kafka_ml1"):
    consumer = KafkaConsumer(
        topic_name,
        group_id="my-group-1",
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for message in consumer:
        data = message.value
        print(f"Received message: {data}")
        
# Llamar a la función del consumidor
kafka_consumer()


#!/usr/bin/env python
import pika
from sys import stdin

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='hello', exchange_type='fanout')



body = "" 

for line in stdin:
    body += line

print(body)
   

channel.basic_publish(exchange='hello', routing_key='', body=body)
connection.close()

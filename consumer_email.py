#!/usr/bin/env python
import pika, sys, os, json
import generic_consumer
from Gmail.gmail import send_email

def callback(ch, method, properties, body):
    print(" [x] Mensaje recibido !! %r" % body)
    data = json.loads(body)
    send_email(data, "cbalbuena@utec.edu.pe")
    print("  ===> Correo enviado ===>")


if __name__ == '__main__':
    cons = generic_consumer.GenericConsumer("hello", callback)
    cons.run()

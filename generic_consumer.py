#!/usr/bin/env python
import pika, sys, os

class GenericConsumer:
    def __init__(self, exchange, callback):
        self.callback = callback
        
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.result = self.channel.queue_declare(queue='', exclusive = True)
        self.queue_name = self.result.method.queue
        self.channel.queue_bind(exchange=exchange, queue=self.queue_name)
        

    def handle(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def run(self):
        try:
            self.handle()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)


import pika, sys, os
from mongo_conenction import insert_data
from generic_consumer import GenericConsumer



def callback(ch,method,properties,body):
    insert_data(body.decode("utf-8"))


cons = GenericConsumer('hello',callback)

cons.run()


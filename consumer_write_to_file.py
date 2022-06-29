#!/usr/bin/env python
from generic_consumer import GenericConsumer



import touch

touch.touch('data.dat')

def callback(ch,method,properties,body):
    file = open('data.dat',mode="a+")
    print(body)
    file.write(str(body))
    file.close()



cons = GenericConsumer('hello',callback)

cons.run()


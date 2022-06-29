#!/usr/bin/env python
from generic_consumer import GenericConsumer



from pathlib import Path
#import touch

#touch.touch('data.dat')
Path('data.dat').touch(exist_ok=True);

def callback(ch,method,properties,body):
    file = open('data.dat',mode="a+")
    print(body)
    file.write(str(body))
    file.close()



cons = GenericConsumer('hello',callback)

cons.run()


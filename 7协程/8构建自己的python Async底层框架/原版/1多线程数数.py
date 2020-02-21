# Build Your Own Async
#
# David Beazley (@dabeaz)
# https://www.dabeaz.com
#
# Originally presented at PyCon India, Chennai, October 14, 2019

import time

def countdown(n):
    while n > 0:
        print('Down', n)
        time.sleep(1)
        n -= 1

def countup(stop):
    x = 0
    while x < stop:
        print('Up', x)
        time.sleep(1)
        x += 1

# Example of sequential execution
countdown(5)
countup(5)

# Example of concurrent execution (via threads)
import threading
threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()
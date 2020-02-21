# aproducer_error.py
#
# Example of returning results + errors in callback based code.

import time
from collections import deque
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque()     # Functions ready to execute
        self.sleeping = []       # Sleeping functions
        self.sequence = 0 

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay     # Expiration time
        # Priority queue
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))
        
    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                # Find the nearest deadline
                deadline, _, func = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(func)

            while self.ready:
                func = self.ready.popleft()
                func()

sched = Scheduler()     # Behind scenes scheduler object

# -----

# Class used to communicate both a normal value or an exception
class Result:
    def __init__(self, value=None, exc=None):
        self.value = value
        self.exc = exc

    def result(self):
        if self.exc:
            raise self.exc
        else:
            return self.value

class AsyncQueue:
    def __init__(self):
        self.items = deque()
        self.waiting = deque()    # All getters waiting for data
        self._closed = False      # Can queue be used anymore?

    def close(self):
        self._closed = True
        if self.waiting and not self.items:
            for func in self.waiting:
                sched.call_soon(func)

    def put(self, item):
        if self._closed:
            raise QueueClosed()

        self.items.append(item)
        if self.waiting:
            func = self.waiting.popleft()
            # Do we call it right away?
            sched.call_soon(func)

    def get(self, callback):
        # Wait until an item is available. Then return it
        # Question: How does a closed queue interact with get()
        if self.items:
            callback(Result(value=self.items.popleft()))  # Good result
        else:
            # No items available (must wait)
            if self._closed:
                callback(Result(exc=QueueClosed())) # Error result
            else:
                self.waiting.append(lambda: self.get(callback))

class QueueClosed(Exception):
    pass

def producer(q, count):
    def _run(n):
        if n < count:
            print('Producing', n)
            q.put(n)
            sched.call_later(1, lambda: _run(n+1))
        else:
            print('Producer done')
            q.close()   # Means no more items will be produced
    _run(0)

def consumer(q):
    def _consume(result):
        try:
            item = result.result()
            print('Consuming', item)   
            sched.call_soon(lambda: consumer(q))
        except QueueClosed:
            print("Consumer done")
    q.get(callback=_consume)

q = AsyncQueue()
sched.call_soon(lambda: producer(q, 10))
sched.call_soon(lambda: consumer(q,))
sched.run()

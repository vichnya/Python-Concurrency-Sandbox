#Программа с собственным классом "очередь" (Queue) и рекурсивным блокировщиком RLock

import threading
import time

class MyQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.RLock()

    def enqueue(self, item):
        with self.lock:
            self.queue.append(item)

    def dequeue(self):
        with self.lock:
            if self.queue:
                return self.queue.pop(0)
            else:
                return None

def queue_operations(queue, num_items):
    for i in range(num_items):
        queue.enqueue(i)
        time.sleep(0.1)

    for _ in range(num_items):
        item = queue.dequeue()
        if item is not None:
            print(f"Dequeued item: {item}")
        time.sleep(0.1)


my_queue = MyQueue()

thread1 = threading.Thread(target=queue_operations, args=(my_queue, 5))
thread2 = threading.Thread(target=queue_operations, args=(my_queue, 5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

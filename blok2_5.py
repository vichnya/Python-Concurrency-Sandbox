#Программа с использованием объекта типа Event

import threading
import time

def set_event(event):
    for _ in range(5):
        time.sleep(1)
        event.set()

def wait_for_event(event):
    while not event.is_set():
        print("Event did not occur")
        time.sleep(1)
    print("Event occurred")


event = threading.Event()

set_event_thread = threading.Thread(target=set_event, args=(event,))
wait_for_event_thread = threading.Thread(target=wait_for_event, args=(event,))

set_event_thread.start()
wait_for_event_thread.start()

set_event_thread.join()
wait_for_event_thread.join()

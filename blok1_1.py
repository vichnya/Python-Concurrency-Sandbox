#Создание нескольких потоков и вывод их имен
import threading

def print_thread_name():
    thread_name = threading.current_thread().name
    print(f"Thread name: {thread_name}")

threads = []

for i in range(5):
    thread = threading.Thread(target=print_thread_name)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
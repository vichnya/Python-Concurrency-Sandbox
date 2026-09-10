#Программа для параллельного поиска файла в директории

import threading
import os
import queue

def search_file(directory, file_name, result_queue):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                result_queue.put(os.path.join(root, file))


directory = "./"
file_to_find = "example.txt"
result_queue = queue.Queue()

num_threads = 4
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=search_file, args=(directory, file_to_find, result_queue))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

if not result_queue.empty():
    print(f"File found: {result_queue.get()}")
else:
    print("File not found.")
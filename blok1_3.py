#Одновременные HTTP-запросы с использованием потоков
import threading
import requests

def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

urls = ["https://www.google.com/", "https://ya.ru/"]

threads = []

for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
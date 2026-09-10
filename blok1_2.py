#Загрузка нескольких файлов с использованием потоков
import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"{filename} downloaded")

urls = ["https://kartinki.pics/uploads/posts/2023-02/1675745742_kartinkin-net-p-khaski-mototsikl-pinterest-51.jpg", "https://kartinki.pics/uploads/posts/2022-12/thumbs/1672133634_kartinkin-net-p-kartinka-fata-krasivo-43.jpg"]
filenames = ["image1.jpg", "image2.jpg"]

threads = []

for url, filename in zip(urls, filenames):
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
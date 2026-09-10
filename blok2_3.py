#Программа для асинхронной загрузки изображений с использованием объектов типа Future и семафора

import threading
import concurrent.futures
import requests
from PIL import Image
from io import BytesIO

def download_image(url, semaphore):
    with semaphore:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.save(f"downloaded_image_{url.split('/')[-1]}.jpg")


image_urls = ["https://kartinki.pics/uploads/posts/2023-12/1703053540_kartinki-pics-p-novogodnyaya-lisa-oboi-1.jpg", "https://kartinki.pics/uploads/posts/2023-12/thumbs/1703056241_kartinki-pics-p-krasivii-snegopad-oboi-2.jpg"]
semaphore = threading.Semaphore(value=2)  

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(download_image, url, semaphore) for url in image_urls]

    for future in concurrent.futures.as_completed(futures):
        future.result()
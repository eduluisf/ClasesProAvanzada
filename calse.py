import requests
import time
from concurrent.futures import (
    ThreadPoolExecutor, as_completed
)

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]

def descargar(url):
    resp = requests.get(url)
    return resp.json()["title"]

inicio = time.time()

with ThreadPoolExecutor(max_workers=5) as pool:
    futuros = {pool.submit(descargar, u): u
               for u in urls}
    for f in as_completed(futuros):
        print(f.result())

fin = time.time()
print(f"Tiempo: {fin - inicio:.2f}s")

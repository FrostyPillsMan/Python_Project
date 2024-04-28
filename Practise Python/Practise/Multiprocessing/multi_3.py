import requests
import time
import os
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

"""
fetching images over the internet by making an HTTP request
"""

img_urls = [
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt2442560%2F&psig=AOvVaw27lFSulD5__9lMQ_6ql7B8&ust=1711346912825000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMCQh5iejIUDFQAAAAAdAAAAABAE"
    "https://www.google.com/url?sa=i&url=http%3A%2F%2Fpeakyblinders.ch.bbc.co.uk%2Fcharacters%2F101559.html&psig=AOvVaw3mks7SxGDzR8YCEEfE6jLB&ust=1711346943346000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNDKt6aejIUDFQAAAAAdAAAAABAE"
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.eonline.com%2Fnews%2F558774%2Fboardwalk-empire-s-final-season-premiere-date-revealed-plus-michael-pitt-wants-nucky-assassinated&psig=AOvVaw171JZvJN3t3_a2EDxrbS6D&ust=1711347070471000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJiYhuOejIUDFQAAAAAdAAAAABAE"
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.independent.co.uk%2Farts-entertainment%2Ftv%2Fnews%2Fthe-irishman-martin-scorsese-boardwalk-empire-stephen-graham-jack-huston-a7947886.html&psig=AOvVaw171JZvJN3t3_a2EDxrbS6D&ust=1711347070471000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJiYhuOejIUDFQAAAAAdAAAAABAP"
]

t1 = time.perf_counter()
print("Downloading images with single process")


def download_img(img_url):
    img_bytes = requests.get(img_url).content
    print("Downloading...")


process_img = [download_img(img) for img in img_urls]

t2 = time.perf_counter()
print(f"Single Process Code Took :{t2-t1} seconds")
print("*" * 50)

t1 = time.perf_counter()
print("Downloading images with Multiprocess")


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    print(f"[Process ID]:{os.getpid()} Downloading..")


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(3) as exe:
        exe.map(download_image, img_urls)


t2 = time.perf_counter()
print(f'Multiprocess Code Took:{t2-t1} seconds')


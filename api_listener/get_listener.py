import time
from threading import Thread

import requests

url = 'http://127.0.0.1:8081'


def get_all():
    def get_request():
        return requests.get(f"{url}/quotes")

    memory = None
    while True:
        if get_request().json() != memory:
            memory = get_request().json()
            print(memory)
            time.sleep(3)
        else:
            time.sleep(3)


Thread(target=get_all).start()

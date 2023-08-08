import asyncio
import time
from threading import Thread
from urllib import request

import requests

url = 'http://127.0.0.1:8081'
quote0 = {"title": "The TEST",
          "content": "Example test!"}


def send_post(quote):
    def post_request(param):
        return requests.post(f'{url}/quotes/add', None, param)

    count = 0
    while count < 5:
        time.sleep(4)
        print(post_request(quote).json())
        count += 1


requests.post(f'{url}/quotes/add', None, quote0)

print(requests.get(f"{url}/quotes/86U7OHG4Q4").json())

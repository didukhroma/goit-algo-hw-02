from queue import Queue
from datetime import datetime
import uuid
import random

queue = Queue()

def generate_request():
    new_request = {"request_id": f"{str(uuid.uuid4())}-{datetime.timestamp(datetime.now())}"}
    queue.put(new_request)
    print(new_request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(request)
    else:
        print("Queue is empty")

for i in range(10):
    generate_request()
    if random.randint(0, 1) == 1:
        print("Processing request")
        process_request()


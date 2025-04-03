from queue import Queue
from datetime import datetime
import uuid

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

while True:
    user_input = input("Generate request? (y/n): ")
    if user_input == "y":
        generate_request()
        process_request()
    elif user_input == "n":
        break




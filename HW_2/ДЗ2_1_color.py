import queue
import time
import random


class Request:
    def __init__(self):
        self.request_queue = queue.Queue()

    # Method for generating requests
    def generate_request(self):
        request_id = random.randint(1, 1000)
        print(f"🟢 Request {request_id} added to the queue")
        self.request_queue.put(request_id)
        # Delay to simulate irregular arrival of requests
        time.sleep(random.uniform(0.9, 1.5))

    # Method for processing requests
    def process_request(self):
        if not self.request_queue.empty():
            request_id = self.request_queue.get()
            print(f"🔴 Request {request_id} is being processed")
            time.sleep(random.uniform(0.9, 1.5))  # Simulating processing time
        else:
            print("🟡 Queue is empty")
            time.sleep(0.5)


# Creating an instance of the Request class
request_handler = Request()

while True:
    choice = random.randint(0, 1)
    if choice:
        request_handler.generate_request()
    else:
        request_handler.process_request()

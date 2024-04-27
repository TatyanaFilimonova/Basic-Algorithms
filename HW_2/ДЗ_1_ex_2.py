"""Home work 1"""
from queue import Queue
import random
import time
from tqdm import tqdm
from colorama import Fore, Style

class ServiceRequestsNotFound(Exception):
    """Exception for request queue"""

class Requests():
    """Service reques queue"""
    def __init__(self, ):
        self.title = random.randint(1111, 9999)

class Service():
    """Service reques queue"""
    def __init__(self, delay=1) -> None:
        self.requests = Queue()
        self.delay = delay

    def generate_request(self, count):
        """
        Створити нову заявку
        Додати заявку до черги
        """
        print(Fore.YELLOW)
        progres = tqdm(range(count))
        for _ in progres:
            request = Requests()
            progres.set_description(f"Creating.... {request.title}")
            self.requests.put(request)
            time.sleep(self.delay/10)

    def process_request(self, count):
        """
        Якщо черга не пуста:
            Видалити заявку з черги
            Обробити заявку
        Інакше:
            Вивести повідомлення, що черга пуста

        """
        print(Fore.GREEN)
        progres = tqdm(range(count))
        for _ in progres:
            if self.requests.empty():
                raise ServiceRequestsNotFound
            cur_request = self.requests.get()
            progres.set_description(f"Processing.. {cur_request.title}")
            time.sleep(self.delay)


def main():
    """
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
    """
    # Створити чергу заявок
    requests = Service(0.5)
    requests.generate_request(9)
    requests.process_request(10)

while True:
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.GREEN + "OK...Bye!")
        break
    except ServiceRequestsNotFound:
        print(Fore.RED + "Warning...request not found!")
        print(Style.RESET_ALL)

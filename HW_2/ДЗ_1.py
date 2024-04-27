from queue import Queue
import time
import random

# Створюємо чергу заявок
request_queue = Queue()

def generate_request():
    """Генерування нової заявки з унікальним ідентифікатором і додавання її в чергу."""
    request_id = random.randint(1000, 9999)  # Рандомний 4-значний ID 
    print(f"Generated request with ID: {request_id}")
    request_queue.put(request_id)

def process_request():
    """Обробка заявки, видалення її з черги, якщо вона доступна."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request with ID: {request_id}")
    else:
        print("The queue is empty, no requests to process.")

# Симуляція формування та обробки заявок
def simulate_service_center(duration=10):
    """Симуляція роботи сервісного центру протягом заданих проміжків часу."""
    start_time = time.time()
    while time.time() - start_time < duration:
        generate_request()  # Генерування нової заявки
        time.sleep(0.5)  # Симуляція часу між створеннями заявок 
        process_request()  # Обробка заявок
        time.sleep(0.5)  # Симуляція часу обробки

# Запуск симуляції
simulate_service_center()

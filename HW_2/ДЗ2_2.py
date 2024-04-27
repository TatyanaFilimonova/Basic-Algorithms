from collections import deque
import string

def is_palindrome(input_string):
    """Перевірка рядка на паліндромність з ігноруванням регістрів та пробілів."""
    # Обробляємо пробіли та нижній регістр
    normalized_string = ''.join(char.lower() for char in input_string if char in string.ascii_letters)
    
    # Додаємо записи
    char_deque = deque(normalized_string)
    
    # Перевіряємо на палндромність, шляхом порівняння з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади виконання функції
test_strings = ["Кит на морі романтик", "І розморозь зором зорі", "А БАБА на волі — цілована баба", "No lemon, no melon", "Hello world"]
results = {s: is_palindrome(s) for s in test_strings}
print(results)

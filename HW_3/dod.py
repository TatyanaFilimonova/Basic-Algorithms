def move_disk(n, from_rod, to_rod, aux_rod, state):
    if n == 1:
        state[from_rod].pop()
        state[to_rod].append(1)
        print(f"Перемістити диск з {from_rod} на {to_rod}: 1")
        print(f"Проміжний стан: {state}")
    else:
        move_disk(n-1, from_rod, aux_rod, to_rod, state)
        state[from_rod].pop()
        state[to_rod].append(n)
        print(f"Перемістити диск з {from_rod} на {to_rod}: {n}")
        print(f"Проміжний стан: {state}")
        move_disk(n-1, aux_rod, to_rod, from_rod, state)

def solve_towers_of_hanoi(n):
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    move_disk(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")

n = int(input("Введіть кількість дисків: "))
solve_towers_of_hanoi(n)

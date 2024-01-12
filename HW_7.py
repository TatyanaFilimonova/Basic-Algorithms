from faker import Faker


# AVL-tree
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = f"\t" * level + prefix + str(self.key) + f"\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


# Task 1
# Finds max value in the Tree
def find_max_value(root):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right

    return current.key


# Task 2
# Finds min value in the Tree
def find_min_value(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.key


# Task 3
# Calculates sum of Tree values
def calculate_tree_sum(root):
    if root is None:
        return 0

    return root.key + calculate_tree_sum(root.left) + calculate_tree_sum(root.right)


# Generate unique random numbers
def generate_unique_random_numbers(num):
    fake = Faker()
    generated_numbers = set()
    while len(generated_numbers) < num:
        random_number = fake.random_int(min=1, max=1000)
        if random_number not in generated_numbers:
            generated_numbers.add(random_number)

    return generated_numbers


# Checks if tree operation is correct
def check_correct_tree_operation(random_number, tree_value, message):
    if random_number == tree_value:
        print(f"{message}: {tree_value}")
    else:
        print(
            f"Value is incorrect. Expected value {random_number}, but got {tree_value}"
        )


random_unique_numbers = generate_unique_random_numbers(20)

print(random_unique_numbers)

root = None

for key in random_unique_numbers:
    root = insert(root, key)
    print("Inserted:", key)
    print("AVL-Tree:")
    print(root)

print("Task 1 - find Max value")
check_correct_tree_operation(
    max(random_unique_numbers), find_max_value(root), "Max value in the AVL-Tree"
)

print("Task 2 - find Min value")
check_correct_tree_operation(
    min(random_unique_numbers), find_min_value(root), "Min value in the AVL-Tree"
)

print("Task 3 - calculate sum of Tree values")
check_correct_tree_operation(
    sum(random_unique_numbers), calculate_tree_sum(root), "Sum of Tree values"
)

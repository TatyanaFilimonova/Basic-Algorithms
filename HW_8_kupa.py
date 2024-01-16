from faker import Faker
import heapq


def minimize_cable_order_connection(cable_lengths):
    heapq.heapify(cable_lengths)

    costs = list()

    while len(cable_lengths) > 1:
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        cost = shortest1 + shortest2
        costs.append(cost)

        heapq.heappush(cable_lengths, cost)

    return costs


# Generate random cable lengths
def generate_random_cable_lengths(num):
    fake = Faker()
    generated_cable_lengths = list()
    while len(generated_cable_lengths) < num:
        random_cable_len = fake.random_int(min=2, max=50)
        generated_cable_lengths.append(random_cable_len)

    return generated_cable_lengths


cables = generate_random_cable_lengths(10)
order_connection = minimize_cable_order_connection(cables)

print(f"Connection order:\n" + " --> ".join([str(order) for order in order_connection]))
print("Minimal costs:", order_connection[0])
print("Total costs:", sum(order_connection))

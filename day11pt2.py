import numpy as np
from typing import Callable


class Monkey:
    def __init__(self,
                 items: list[int],
                 operation: Callable[[int], int],
                 test: Callable[[int], bool],
                 destination: list[int]):
        self.items = items
        self.operation = operation
        self.test = test
        self.destination = destination
        self.inspections = 0

    def catch_item(self, new_item):
        self.items.append(new_item)

    def action(self) -> list[tuple[int, int]]:
        # inspect the items
        for i in range(len(self.items)):
            self.items[i] = self.operation(self.items[i]) % 9699690
        # test the items
        thrown_items = list()
        self.inspections += len(self.items)
        for i in range(len(self.items)):
            if self.test(self.items[i]):
                thrown_items.append((self.items[i], self.destination[0]))
            else:
                thrown_items.append((self.items[i], self.destination[1]))
        # monkey has thrown all items
        self.items.clear()
        return thrown_items

    def __repr__(self):
        return self.items.__repr__()


jungle = [Monkey([79, 98],
                 lambda x: x * 19, lambda x: x % 23 == 0, [2, 3]),
          Monkey([54, 65, 75, 74],
                 lambda x: x + 6, lambda x: x % 19 == 0, [2, 0]),
          Monkey([79, 60, 97],
                 lambda x: x * x, lambda x: x % 13 == 0, [1, 3]),
          Monkey([74],
                 lambda x: x + 3, lambda x: x % 17 == 0, [0, 1])]

np.lcm.reduce([23, 19, 13, 17])

rounds = 10000
for i in range(rounds):
    for monkey in jungle:
        thrown_items = monkey.action()
        for item in thrown_items:
            jungle[item[1]].catch_item(item[0])

for i in range(len(jungle)):
    print(f"Monkey {i} has inspected items {jungle[i].inspections} times!")


myjungle = [Monkey([97, 81, 57, 57, 91, 61],
                   lambda x: x * 7, lambda x: x % 11 == 0, [5, 6]),
            Monkey([88, 62, 68, 90],
                   lambda x: x * 17, lambda x: x % 19 == 0, [4, 2]),
            Monkey([74, 87],
                   lambda x: x + 2, lambda x: x % 5 == 0, [7, 4]),
            Monkey([53, 81, 60, 87, 90, 99, 75],
                   lambda x: x + 1, lambda x: x % 2 == 0, [2, 1]),
            Monkey([57],
                   lambda x: x + 6, lambda x: x % 13 == 0, [7, 0]),
            Monkey([54, 84, 91, 55, 59, 72, 75, 70],
                   lambda x: x * x, lambda x: x % 7 == 0, [6, 3]),
            Monkey([95, 79, 79, 68, 78],
                   lambda x: x + 3, lambda x: x % 3 == 0, [1, 3]),
            Monkey([61, 97, 67],
                   lambda x: x + 4, lambda x: x % 17 == 0, [0, 5])]

np.lcm.reduce([11, 19, 5, 2, 13, 7, 3, 17])

rounds = 10000
for i in range(rounds):
    for monkey in myjungle:
        thrown_items = monkey.action()
        for item in thrown_items:
            myjungle[item[1]].catch_item(item[0])

for i in range(len(myjungle)):
    print(f"Monkey {i} has inspected items {myjungle[i].inspections} times!")

total_inspections = []
for monkey in myjungle:
    total_inspections.append(monkey.inspections)

print(np.sort(total_inspections))

print(13954061248)

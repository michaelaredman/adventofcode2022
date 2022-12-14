
from functools import cmp_to_key

packets = []
with open('inputs/day13', 'r') as f:
    temp = []
    for line in f:
        if line != '\n':
            exec("temp = " + line)
            packets.append(temp)


def check_order(left, right) -> bool | None:
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        elif left < right:
            return True
        else:
            return False
    elif isinstance(left, int):
        return check_order([left], right)
    elif isinstance(right, int):
        return check_order(left, [right])
    else:
        i = 0
        while True:
            if i == len(left) and i == len(right):
                return None
            elif i == len(left):
                return True
            elif i == len(right):
                return False

            sub_order = check_order(left[i], right[i])
            if sub_order == True:
                return True
            elif sub_order == False:
                return False
            i += 1
    return None


right_order_sum = 0

packets_iter = iter(packets)
for pair in range(len(packets)//2):
    left = next(packets_iter)
    right = next(packets_iter)
    if check_order(left, right):
        right_order_sum += (pair + 1)

print(f"The sum of the indicies in the right order is {right_order_sum}.")


def order_cmp(left, right):
    order = check_order(left, right)
    if order == None:
        return 1
    else:
        return -1 if order else 1


distress_signal = 1

packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(order_cmp))
for i, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        distress_signal *= (i + 1)

print(f"The distress signal is {distress_signal}.")

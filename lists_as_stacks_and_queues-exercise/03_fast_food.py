from collections import deque

foodQuantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while len(orders) != 0:
    order = orders[0]
    if order > foodQuantity:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
    else: 
        foodQuantity -= order
    orders.popleft();

if len(orders) == 0:
    print("Orders complete")
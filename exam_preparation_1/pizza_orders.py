from collections import deque

pizza_orders = [int(num) for num in input().split(", ")]
employees = [int(num) for num in input().split(", ")]

pizza_orders = deque(pizza_orders)
employees = deque(employees)

total_pizzas = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()

    if order < 0 or order > 10:
        continue

    capacity = 0

    while capacity < order and employees:
        employee = employees.pop()
        capacity += employee

    if not employees and capacity < order:
        orders_left = order - capacity
        pizza_orders.appendleft(orders_left)
    
    total_pizzas += order

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(p) for p in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(e) for e in employees)}")

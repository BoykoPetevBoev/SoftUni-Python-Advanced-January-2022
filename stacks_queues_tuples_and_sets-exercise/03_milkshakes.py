from collections import deque

chocolate = [int(i) for i in input().split(", ")]
milk = deque([int(i) for i in input().split(", ")])

milkshakes_order = 0

for index, number in enumerate(reversed(chocolate)):
    if (number <= 0 or milk[0] <= 0):
        if number <= 0:
            chocolate.pop()
        if milk and milk[0] <= 0:
            milk.popleft()
    elif (number == milk[0]):
        milkshakes_order += 1
        chocolate.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        chocolate[index] = chocolate[index] - 5
    
    if (milkshakes_order == 5):
        print("Great! You made all the chocolate milkshakes needed!")
        break
 
    if(not milk):
        break

if (milkshakes_order != 5):
    print("Not enough milkshakes.")

chocolate_result = ', '.join(map(str, chocolate))
if (chocolate_result == ""):
    chocolate_result = "empty"
print(f"Chocolate: {chocolate_result}")

milk_result = ', '.join(map(str, milk))
if (milk_result == ""):
    milk_result = "empty"
print(f"Milk: {milk_result}")

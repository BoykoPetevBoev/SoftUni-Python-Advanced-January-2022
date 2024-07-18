from collections import deque

num = int(input())

parking = deque()

for _ in range(num):
    direction, car = input().split(", ")

    if direction == "IN"  and car not in parking:
        parking.append(car)
    elif direction == "OUT" and car in parking:
        parking.remove(car)

if parking:
    print(*parking, sep="\n")
else :
    print("Parking Lot is Empty")
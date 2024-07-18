from collections import deque

liters = int(input())
peoples = deque()

command = input()
while not command == "Start":
    peoples.append(command)
    command = input()

command = input()
while not command == "End":
    if command.isdigit():
        required_liters = int(command)
        if required_liters <= liters:
            liters -= required_liters
            print(f"{peoples.popleft()} got water")
        else:
            print(f"{peoples.popleft()} must wait")
    elif command.startswith("refill"):
        _, liters_to_fill = command.split()
        liters += int(liters_to_fill)
    command = input()

print(f"{liters} liters left")

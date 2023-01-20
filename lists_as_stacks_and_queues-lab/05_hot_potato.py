from collections import deque

names = input()
steps = int(input())

peoples = deque(names.split(" "))

while not len(peoples) == 1:
    for i in range(steps - 1):
        name = peoples.popleft()
        peoples.append(name)
    name = peoples.popleft()
    print(f"Removed {name}")

name = peoples.popleft()
print(f"Last is {name}")

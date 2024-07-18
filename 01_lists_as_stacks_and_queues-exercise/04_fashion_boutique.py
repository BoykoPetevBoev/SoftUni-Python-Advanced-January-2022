from collections import deque

clothes = deque([int(x) for x in input().split()])
capacity = int(input())

used_racks = 1
current_rack = capacity

while clothes:
    current = clothes.pop()
    if(current <= current_rack):
        current_rack -= current
    else:
        used_racks += 1
        current_rack = capacity - current

print(used_racks)

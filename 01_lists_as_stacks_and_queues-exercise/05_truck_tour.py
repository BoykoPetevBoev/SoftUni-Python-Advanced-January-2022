from collections import deque

petrol_pumps = int(input())

current_petrol = 0
pumps = deque();
start = -1

while petrol_pumps:
    petrol, distance = input().split()
    pumps.append([int(petrol), int(distance)])
    petrol_pumps -=1

for start_pump in range(len(pumps)):
    tank = 0
    for petrol, distance in pumps:
        tank += petrol - distance
        if(tank < 0): 
            break
    
    if(tank >= 0):
        start = start_pump
        break

    pump = pumps.popleft()
    pumps.append(pump)

print(start)
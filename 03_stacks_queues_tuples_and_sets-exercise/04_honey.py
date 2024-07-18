from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

while nectars and bees:

    bee = bees[0]
    nectar = nectars.pop()

    if bee > nectar:
        continue

    bee = bees.popleft()
    sym = symbols.popleft()
    if sym == "+":
        honey += abs(bee + nectar)
    elif sym == "-":
        honey += abs(bee - nectar)
    elif sym == "*":
        honey += abs(bee * nectar)
    elif sym == "/" and nectar > 0:
        honey += abs(bee / nectar)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")

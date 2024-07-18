num = int(input())

result = []

for _ in range(num):
    name = input()
    if name not in result:
        result.append(name)

print(*result, sep="\n")
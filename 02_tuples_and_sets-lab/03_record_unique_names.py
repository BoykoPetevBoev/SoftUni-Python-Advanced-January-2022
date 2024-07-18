num = int(input())

result = set()

for _ in range(num):
    name = input()
    result.add(name)

print(*result, sep="\n")
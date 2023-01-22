num = int(input())

result = set()

for _ in range(num):
    chemicals = input().split()
    for chemical in chemicals:
        result.add(chemical)

print("\n".join(result))

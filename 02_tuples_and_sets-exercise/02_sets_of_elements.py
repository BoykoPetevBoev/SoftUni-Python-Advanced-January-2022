n, m = (int(el) for el in input().split())

first_set = set()
second_set = set()

for _ in range(n):
    num = input()
    first_set.add(num)

for _ in range(m):
    num = input()
    second_set.add(num)

resilt =  first_set.intersection(second_set)
print("\n".join(resilt))
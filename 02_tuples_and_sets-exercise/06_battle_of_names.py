num = int(input())

row = 1
odd_set = set()
even_set = set()

for _ in range(num):
    name = input()
    name_value = int(0)
    for char in name:
        num = ord(char)
        name_value += num
    
    value = int(name_value / row)
    if(int(value) % 2 == 0):
        even_set.add(value)
    else:
        odd_set.add(value)
    row += 1

if(sum(odd_set) == sum(even_set)):
    res = odd_set.union(even_set)
    print(*res, sep=", ")
elif(sum(odd_set) > sum(even_set)):
    res = odd_set.difference(even_set)
    print(*res, sep=", ")
else:
    res = odd_set.symmetric_difference(even_set)
    print(*res, sep=", ")
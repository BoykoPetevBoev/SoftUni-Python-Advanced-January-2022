lines = int(input())

numbers = []
result = []

while lines != 0:
    line = input()
    lines -= 1
    if line.startswith("1"):
        _, string = line.split()
        num = int(string)
        numbers.append(num)
    elif line == "2" and len(numbers):
        numbers.pop()
    elif line == "3" and len(numbers):
        print(max(numbers))
    elif line == "4" and len(numbers):
        print(min(numbers))

numbers.reverse()

for num in numbers:
    result.append(str(num))


print(", ".join(result))
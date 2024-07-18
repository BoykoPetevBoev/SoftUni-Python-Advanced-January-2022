string = input()

result = {}

for char in string:
    if char not in result:
        result[char] = 0
    result[char] += 1

sortedChars = list(result.keys())
sortedChars.sort()

for char in sortedChars:
    print(f"{char}: {result[char]} time/s")
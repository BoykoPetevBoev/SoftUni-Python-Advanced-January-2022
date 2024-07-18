expression = input()

indexes = []

for i in range(len(expression)):
    if expression[i] == "(":
        indexes.append(i)
    elif expression[i] == ")":
        start_index = indexes.pop()
        print(expression[start_index: i + 1])

# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
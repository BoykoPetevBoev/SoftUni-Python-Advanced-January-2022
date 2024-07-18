import math

expressions = input().split()
stack = []

for sym in expressions:
    if sym in ["*", "/", "+", "-"]:
        result = 0
        if sym == "+":
            result = sum(stack)
        elif sym == "*":
            result = 1
            for number in stack:
                result *= number
        elif sym == "/":
            result = stack[0]
            for number in stack[1:]:
                result /= number
                result = math.floor(result)
        elif sym == "-":
            result = stack[0]
            for number in stack[1:]:
                result -= number
        stack = [result]
    else:
        stack.append(int(sym))

print(stack[0])
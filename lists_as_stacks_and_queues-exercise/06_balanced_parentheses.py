from collections import deque

parenthesis = input()

brackets = []
is_balanced = "YES"

for char in parenthesis:
    if char in "({[":
        brackets.append(char)
    else:
        if not brackets:
            is_balanced = "NO"
            break
        open_char = brackets.pop()
        if (
                open_char == "(" and char == ")"
            ) or (
                open_char == "{" and char == "}"
            ) or (
                open_char == "[" and char == "]"
            ):
            continue
        else: 
            is_balanced = "NO"
            break

print(is_balanced)


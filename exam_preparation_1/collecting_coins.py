import math

size = int(input())

matrix = []

row_position = 0
col_position = 0
total_coins = 0

player_path = []

for row_idx in range(size):
    row = input().split(" ")
    matrix.append(row)

    if row.count("P") == 1:
        col_idx = row.index("P")
        row_position = row_idx
        col_position = col_idx
        matrix[row_idx][col_idx] = 0

player_path.append([row_position, col_position])

while True:
    command = input()

    if command == "up":
        row_position -= 1
        if row_position < 0:
            row_position = size - 1

    elif command == "down":
        row_position += 1
        if row_position >= size:
            row_position = 0

    elif command == "left":
        col_position -= 1
        if col_position < 0:
            col_position = size - 1

    elif command == "right":
        col_position += 1
        if col_position >= size:
            col_position = 0

    player_path.append([row_position, col_position])
    field_value = matrix[row_position][col_position] 

    if field_value == "X":
        total_coins = math.floor(total_coins / 2)
        print(f"Game over! You've collected {total_coins} coins.")
        break

    total_coins += int(field_value)
    matrix[row_position][col_position] = 0

    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        break

print("Your path:")
for row in player_path:
    print(f"[{str(row[0])}, {str(row[1])}]")
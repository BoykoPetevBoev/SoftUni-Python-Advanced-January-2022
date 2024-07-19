size = int(input())
bombs = int(input())

matrix = [[0 for col in range(size)] for row in range(size)]

for _ in range(bombs):
    row, col = map(int, input().strip("()").split(", "))

    matrix[row][col] = "*"

    for y in [row - 1, row, row + 1]:
        for x in [col - 1, col, col + 1]:
            if(x < 0 or y < 0 or x >= size or y >= size or matrix[y][x] == "*"):
                continue
            matrix[y][x] += 1

for row in matrix:
    print(" ".join([str(num) for num in row]))

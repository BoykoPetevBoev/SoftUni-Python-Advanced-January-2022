class Pawn:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.captures = False 
        self.promoted = False

    def get_position(self):
        cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
        return f"{cols[self.col]}{8 - self.row}"


def get_chessboard():
    chessboard = []
    for row in range(8):
        line = input().split(" ")
        if line.count("b"):
            black_col = line.index("b")
            black_pawn = Pawn(row, black_col)
        if line.count("w"):
            white_col = line.index("w")
            white_pawn = Pawn(row, white_col)
        chessboard.append(line)
    return chessboard, white_pawn, black_pawn


def move_white_pawn(chessboard, white_pawn):
    next_row = white_pawn.row - 1
    next_col = white_pawn.col

    if white_pawn.col > 0:
        col = white_pawn.col - 1
        if chessboard[next_row][col] == "b":
            next_col = col 
            white_pawn.captures = True
        
    if white_pawn.col < 7:
        col = white_pawn.col + 1
        if chessboard[next_row][col] == "b":
            next_col = col
            white_pawn.captures = True
        
    if next_row == 0:
        white_pawn.promoted = True
    
    chessboard[white_pawn.row][white_pawn.col] = "-"
    white_pawn.row = next_row
    white_pawn.col = next_col
    chessboard[white_pawn.row][white_pawn.col] = "w"



def move_black_pawn(chessboard, black_pawn):
    next_row = black_pawn.row + 1
    next_col = black_pawn.col

    if black_pawn.col > 0:
        col = black_pawn.col - 1
        if chessboard[next_row][col] == "w":
            next_col = col 
            black_pawn.captures = True
        
    if black_pawn.col < 7:
        col = black_pawn.col + 1
        if chessboard[next_row][col] == "w":
            next_col = col
            black_pawn.captures = True
        
    if next_row == 0:
        black_pawn.promoted = True

    chessboard[black_pawn.row][black_pawn.col] = "-"
    black_pawn.row = next_row
    black_pawn.col = next_col
    chessboard[black_pawn.row][black_pawn.col] = "b"



def play_chess_game():
    chessboard, white_pawn, black_pawn = get_chessboard()
    play_game = True

    while play_game:
        move_white_pawn(chessboard, white_pawn)

        if white_pawn.captures:
            print(f"Game over! White win, capture on {white_pawn.get_position()}.")
            play_game = False
            break

        if white_pawn.promoted:
            print(f"Game over! White pawn is promoted to a queen at {white_pawn.get_position()}.")
            play_game = False
            break

        move_black_pawn(chessboard, black_pawn)

        if black_pawn.captures:
            print(f"Game over! Black win, capture on {black_pawn.get_position()}.")
            play_game = False
            break
        
        if black_pawn.promoted:
            print(f"Game over! Black pawn is promoted to a queen at {black_pawn.get_position()}.")
            play_game = False
            break

play_chess_game()


from collections import deque

bomb_effects = [int(num) for num in input().split(", ")]
bomb_casing = [int(num) for num in input().split(", ")]

bomb_effects = deque(bomb_effects)
bomb_casing = deque(bomb_casing)

datura_bombs = 40
cherry_bombs = 60
smoke_decoy_bombs = 120

datura_bombs_count = 0
cherry_bombs_count = 0
smoke_decoy_bombs_count = 0

while bomb_casing and bomb_effects:
    if datura_bombs_count >= 3 and cherry_bombs_count >= 3 and smoke_decoy_bombs_count >= 3:
        break
    
    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casing = bomb_casing.pop()

    bomb = first_bomb_effect + last_bomb_casing

    if bomb == datura_bombs:
        datura_bombs_count += 1
    elif bomb == cherry_bombs:
        cherry_bombs_count += 1
    elif bomb == smoke_decoy_bombs:
        smoke_decoy_bombs_count += 1
    else:
        bomb_effects.appendleft(first_bomb_effect)
        bomb_casing.append(last_bomb_casing - 5)
    

if datura_bombs_count >= 3 and cherry_bombs_count >= 3 and smoke_decoy_bombs_count >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(bomb) for bomb in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(bomb) for bomb in bomb_casing])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs_count}")
print(f"Datura Bombs: {datura_bombs_count}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs_count}")
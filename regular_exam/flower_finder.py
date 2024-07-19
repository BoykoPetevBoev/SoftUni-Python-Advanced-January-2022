from collections import deque
from regular_exam.flower_finder_class import Flower

found_flower = None
vowels = deque(input().split(" "))
consonants = deque(input().split(" "))
valid_flowers = [Flower("rose"), Flower("tulip"), Flower("lotus"), Flower("daffodil")]

while vowels and consonants and not found_flower:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    for flower in valid_flowers:
        flower.check_letter(first_vowel)
        flower.check_letter(last_consonant)

        if flower.is_found():
            found_flower = flower


if found_flower:
    print(f"Word found: {found_flower.name}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
chars_to_change = ['-', ',', '.', '!', '?']

try: 
    with open('text.txt', 'r') as file:
        for row, line in enumerate(file):
            if row % 2 == 0:
                result = ' '.join(line.strip().split()[::-1])
                for char in chars_to_change:
                    result = result.replace(char, '@')
                print(result)
except FileExistsError:
    print("No such file or directory")
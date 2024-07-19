class Flower:
    def __init__(self, name):
        self.name = name
        self.found_letters = []

    def check_letter(self, letter):
        if letter in self.name and letter not in self.found_letters:
            self.found_letters.append(letter)

    def is_found(self):
        return len(set(self.found_letters)) == len(set(self.name))

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)
    
    def print(self):
        print(self.letters)
    
    def letters_num(self):
        return len(self.letters)

import string

class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)
    
    def is_en_letter(self, letter):
        return letter.upper() in self.letters
    
    def letters_num(self):
        return self._letters_num
    
    @staticmethod
    def example():
        return "English Example:\nDon't judge a book by it's cover."

eng_alphabet = EngAlphabet()

eng_alphabet.print()  # Виведе: ['A', 'B', 'C', 'D', ..., 'Z']

print(eng_alphabet.letters_num())  # Виведе: 26

print(eng_alphabet.is_en_letter('F'))  # Виведе: True

print(eng_alphabet.is_en_letter('Щ'))  # Виведе: False

print(EngAlphabet.example())  # Виведе: "English Example: Don't judge a book by it's cover."

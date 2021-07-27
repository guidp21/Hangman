import json
from random import choice
import string

class Hangman:

    def __init__(self):
        self.WORDS_FILE = "words.json"
        self.life = 10
        self.alphabet = set(string.ascii_uppercase)
        self.word = self.get_word()
        self.word_letters = set(self.word)
        self.used_letters = set()

    def load_words(self): # load all the words of the words file
        with open(self.WORDS_FILE, 'r') as f:
            return json.load(f)
        
    def get_word(self): # choose a random word from the words file
        WORDS = self.load_words()
        random_word = choice(WORDS)

        # only choose words without "-" or " "
        while "-" in random_word and " " in random_word: 
            random_word = choice(WORDS)

        return random_word
    
    def input_letter(self): # input users attempt
        while True:
            letter_input = str(input("Guess a letter: ")).strip().upper()[0]

            # if it's in the alphabet and hasn't been used yet
            if letter_input in self.alphabet - self.used_letters:
                self.used_letters.add(letter_input)

                return letter_input
            
            else:
                print("Invalid input! Try again.")
            

    

    


    

        
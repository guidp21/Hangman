import json
from random import choice

class Hangman:

    def __init__(self, WORDS_FILE):
        self.WORDS_FILE = WORDS_FILE
        self.life = 10

    def load_words(self): # load all the words of the words file
        with open(self.WORDS_FILE, 'r') as f:
            return json.load(f)
        
    def choose_word(self): # choose a random word from the words file
        WORDS = self.load_words()
        random_word = choice(WORDS)

        # only choose words without "-" or " "
        while "-" in random_word and " " in random_word: 
            random_word = choice(WORDS)

        return random_word
    


    

        
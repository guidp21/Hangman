import json
from random import choice
import string

class Hangman:

    def __init__(self):
        self.WORDS_FILE = "words.json"
        self.life = 10
        self.alphabet = set(string.ascii_uppercase)
        self.word = self.get_word()
        self.word_letters = list(self.word)
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

        return random_word.upper()
    
    def input_letter(self): # input users attempt
        while True:
            letter_input = str(input("Guess a letter: ")).strip().upper()[0]

            # if it's in the alphabet and hasn't been used yet
            if letter_input in self.alphabet - self.used_letters:
                self.used_letters.add(letter_input)

                return letter_input
            
            # letter has already been already used
            elif letter_input in self.used_letters:
                print("You have already used this letter. Please try again.")
            
            # number
            else:
                print("Invalid input! Try again.")
    
    def analyse_input_letter(self, letter_input):
        print(f"{letter_input} {self.word_letters}")
        # right letter
        if letter_input in self.word_letters:
            self.word_letters.remove(letter_input)
            print("right letter")

        # wrong letter
        else:
            self.life -= 1
            print("wrong letter")
    
    def check_game_status(self): # check victory or defeat
        # playing
        if self.life > 0:

            # victory
            if len(self.word_letters) == 0:
                print("You won")
                return False
            
            # still playing
            else:
                return True

        # defeat
        else:
            print("You lost!")
            return False
    
    def used_letters_indicator(self): # show the user which letters were used
        if len(self.used_letters) > 0:
            print("You had used these letters: ", " ".join(self.used_letters))
        else:
            print("You hadn't used any letter yet.")
    
    def current_word(self): # # show the user the word he's trying to guess
        word_list = list()

        for letter in self.word:

            if letter in self.used_letters:
                word_list.append(letter)
            else:
                word_list.append("_")

        print("Current word: ", " ".join(word_list))


            

    

    


    

        
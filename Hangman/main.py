from hangman import *

HANGMAN = Hangman()

def main():
    print(HANGMAN.word)
    print(HANGMAN.word_letters)
    HANGMAN.input_letter()
    

if __name__ == '__main__':
    main()
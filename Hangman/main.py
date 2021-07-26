from hangman import *

HANGMAN = Hangman("words.json")

def main():
    word = HANGMAN.choose_word()
    print(word)

if __name__ == '__main__':
    main()
from hangman import *

HANGMAN = Hangman()

def main():
    print(HANGMAN.word)
    print(HANGMAN.word_letters)
    playing = True
    while playing:
        HANGMAN.used_letters_indicator()
        HANGMAN.current_word()
        letter_input = HANGMAN.input_letter()
        HANGMAN.analyse_input_letter(letter_input)
        playing = HANGMAN.check_game_status()

if __name__ == '__main__':
    main()
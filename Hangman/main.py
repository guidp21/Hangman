from hangman import *
import os

HANGMAN = Hangman()

def main():
    playing = True

    while playing:
        # clean the cmd
        HANGMAN.refresh_cmd()

        # interface
        HANGMAN.life_indicator()
        HANGMAN.used_letters_indicator()
        HANGMAN.current_word()

        # user input
        letter_input = HANGMAN.input_letter()
        HANGMAN.analyse_input_letter(letter_input)

        # check victory or defeat
        playing = HANGMAN.check_game_status()

if __name__ == '__main__':
    main()
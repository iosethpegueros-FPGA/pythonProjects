# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 18:21:44 2026

@author: ioseth ibis pegueros lepe
"""

from hangman import * #has_player_won
import string
import random 

def main():
    
    print('ps2a hangman with functions')
    
    #testing_print():
    guesses_left=10
    letters_guessed = []
    game_done=False
    player_won=False
    
    exit_game=False

    
    #print(secret_word)
    while(exit_game == False ):
        continue_game =False
        secret_word   =choose_word(wordlist)
        print("I am thinking of a word that is ",len(secret_word),"letters long.")
        hangman(secret_word, 0)
        
        while(continue_game==False):
            continue_game = input ("would you like to play again?? y or n:")
            continue_game = continue_game.lower() if continue_game.isupper() else continue_game
            if continue_game.isalpha() == False:
                    print("please enter a valid character")
                    print("please select y (yes) to continue  or n (to exit game)")
                    continue_game = False
            if continue_game == "y":
                continue_game = True
            elif continue_game == "n":
                continue_game = True
                exit_game     = True        
    return 0



def testing_print():
    secret_word="apple"
    letters_guessed = ["a","p","p","l","e","s"]
    print(has_player_won(secret_word, letters_guessed))
    print(get_word_progress(secret_word, letters_guessed))
    print(get_available_letters(letters_guessed))

    

    string1="HolaAcdEf"
    print(string1.isalpha())
    print(string1.lower())
    
    userInput=['a','C']
        
    char1=userInput[1].lower()
    print(char1)
    
    
    print(choose_word(wordlist))
    
if __name__ == '__main__':
        main()
    
    
    
# Welcome to Hangman!
# I am thinking of a word that is 4 letters long.
# -------------

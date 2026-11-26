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
        
    secret_word=choose_word(wordlist)
    guesses_left=10
    letters_guessed = []
    game_done=False
    player_won=False
    
    #print(secret_word) 
    
    print("I am thinking of a word that is ",len(secret_word)," letters long.")
    
    while(game_done==False):
        print("-----------------")
        print("you have ",guesses_left,"guesses left")
        print("available letters:")
    
        print(get_available_letters(letters_guessed))
    
        letter='*'
        while(letter.isalpha()==False or len(letter)!=1):
            letter=input("Please guess a letter: ")
            if letter.isalpha() ==False or len(letter)!=1:
                print("please enter a valid single ascii character ",letter," is not valid")
            else:
                letters_guessed.append(letter)
        print("the alphabet",get_word_progress(secret_word, letters_guessed))
        player_won =has_player_won(secret_word, letters_guessed)
        game_done = True if guesses_left == 0 or player_won  else False
        guesses_left -=1
        
    
    if player_won == True:
        print("you won with ",guesses_left," guesses left")
        print("you word: ",get_word_progress(secret_word, letters_guessed))
    else:
        print("no guesses left , try again : )")
        print("word was",secret_word)



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

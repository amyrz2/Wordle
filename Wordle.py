# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS,CORRECT_COLOR,PRESENT_COLOR,MISSING_COLOR

global i
i = 0

def wordle():

    def enter_action(s):
        global i
        col = 0
        row = i
        guessed_word = gw.get_square_letter(row,0)+ gw.get_square_letter(row,1)+ gw.get_square_letter(row,2)+ gw.get_square_letter(row,3)+gw.get_square_letter(row,4)
        print(guessed_word)
        if guessed_word.lower() in FIVE_LETTER_WORDS:
            while col < N_COLS :
                if guessed_word[col] == Word[col]:
                    gw.set_square_color(row,col,color=CORRECT_COLOR)
                elif guessed_word[col] in Word:
                    gw.set_square_color(row,col,color=PRESENT_COLOR)
                else:
                    gw.set_square_color(row,col,color=MISSING_COLOR)
                
                col = col + 1

            gw.show_message("Awesome!")
        else: 
            gw.show_message("That is not a real 5 letter word")
        gw.set_current_row(row+1) 

        i = i + 1
       
  

    Word = random.choice(FIVE_LETTER_WORDS)
    Word = Word.upper()
    print(Word)

    


    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()


    ## add anoyherchecker for hte key action
    ## unicaode charactosrs they are chiecking for, you can add another one or change it. 

# File: Wordle.py

import random
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from WordleDictionary import ENG_FIVE_LETTER_WORDS, JAP_FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

global Word

def wordle():
    # This is a pop-up that opens on program start
    root1 = tk.Tk()

    def ENG():
        #do stuff if the user says yes
        global wordDictionary
        wordDictionary = ENG_FIVE_LETTER_WORDS
        root1.destroy()
        # Randomly choose the Wordle from the dictionary
        global Word
        Word = random.choice(wordDictionary).upper()
        print(Word) # For debugging

    def JAP():
        #do stuff if the user says no
        global wordDictionary
        wordDictionary = JAP_FIVE_LETTER_WORDS
        root1.destroy()
        # Randomly choose the Wordle from the dictionary
        global Word
        Word = random.choice(wordDictionary).upper()
        print(Word) # For debugging
    

    def modal1(question):

        label = tk.Label(root1, text=question)

        bYes = tk.Button(root1, text="English ", command=ENG)
        bNo = tk.Button(root1, text="Japanese", command=JAP)

        for el in [label, bYes, bNo]:
            el.pack()

    modal1("What langage would you like to play in?")


    # Initialize global row variable
    global row
    row = 0

    
    def enter_action(s):
        global row
        row = row
        col = 0 # Initialize column
        

        # Retrieve guessed word from WordleGWindow
        guessed_word = gw.get_square_letter(row,0)+ gw.get_square_letter(row,1)+ gw.get_square_letter(row,2)+ gw.get_square_letter(row,3)+gw.get_square_letter(row,4)
        #print(guessed_word) # For debugging

        # Check if player perfectly guessed the Wordle
        if guessed_word == Word:
            for x in range(0, N_COLS): # Iterate through all columns and color all squares CORRECT_COLOR
                gw.set_square_color(WordleGWindow.get_current_row(gw), x, gw._CORRECT_COLOR)
            gw._GAME_OVER = True # sets game_over to true to disable input
            gw.show_message("Winner winner chicken dinner!")
        else: # Player didn't perfectly guess the Wordle
            if guessed_word.lower() in wordDictionary: # If guessed word is a valid word
                while col < N_COLS : # Iterate through columns of guessed word
                    if guessed_word[col] == Word[col]: # If current column's letter in guessed word equals current column's letter in the Wordle
                        gw.set_square_color(row,col,color=gw._CORRECT_COLOR)
                        gw.set_key_color(guessed_word[col],color=gw._CORRECT_COLOR)
                        #print("\"" + guessed_word[col] + "\" is correct") # For debugging
                    elif guessed_word[col] in Word: # If current column's letter in guessed word is present somewhere in the Wordle
                        gw.set_square_color(row,col,color=gw._PRESENT_COLOR)
                        gw.set_key_color(guessed_word[col],color=gw._PRESENT_COLOR)
                        #print("\"" + guessed_word[col] + "\" is somwhere in \"" + Word + "\"") # For debugging
                    else: # Letter in guessed word is neither correct nor present in the Wordle
                        gw.set_square_color(row,col,color=gw._MISSING_COLOR)
                        gw.set_key_color(guessed_word[col],color=gw._MISSING_COLOR)
                        #print("\"" + guessed_word[col] + "\" is not found in \"" + Word + "\"") # For debugging
                    
                    col += 1 # Increment column number

                # Check if this was player's last guess
                if WordleGWindow.get_current_row(gw) == (N_ROWS - 1):
                    gw.show_message("You ran out of guesses! The Wordle was: \"" + Word + "\"")
                    gw._GAME_OVER = True # sets game_over to true to disable input
                else:
                    # Show player how many guesses they have left
                    gw.show_message("Good guess! You have " + str((N_ROWS - 1) - row) + " guesses left.")
                    row += 1 # Increment row number
                    gw.set_current_row(row) # Continue to next row
                
            else: # Guessed word is invalid
                gw.show_message("\"" + guessed_word + "\" is not a real 5 letter word")
                # Row will stay the same here so that the player can backspace and enter a new word
        

    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()

    ## add anoyherchecker for hte key action
    ## unicaode charactosrs they are chiecking for, you can add another one or change it. 

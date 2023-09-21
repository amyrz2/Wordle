# File: Wordle.py

import random
import tkinter as tk



from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS







def wordle():

    # this is a pop up window
    root = tk.Tk()

    global CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
    CORRECT_COLOR = "#66BB66"       # Light green for correct letters
    PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
    MISSING_COLOR = "#999999"       # Gray for letters that don't appear


    def yes():
        #do stuff if the user says yes
        global CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
        CORRECT_COLOR = "#66BB66"       # Light green for correct letters
        PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
        MISSING_COLOR = "#999999"       # Gray for letters that don't appear
        root.destroy()

    def no():
        #do stuff if the user says no
        global CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
        CORRECT_COLOR = "#800080"       # Purple for correct letters
        PRESENT_COLOR = "#0000ff"       # Blue for misplaced letters
        MISSING_COLOR = "#CCAC93"       # Brown for letters that don't appear
        root.destroy() 
    

    def modal(question):

        label = tk.Label(root, text=question)

        bYes = tk.Button(root, text="Correct = Green / Right letter wrong place = Yellow / Not inthe word = Gray", command=yes)
        bNo = tk.Button(root, text="Correct = Purple / Right letter wrong place = Blue / Not in the word = Brown", command=no)

        for el in [label, bYes, bNo]:
            el.pack()

    modal("What color scheme would you like?")


    # Initialize global row variable
    global row
    row = 0

    
    def enter_action(s):
        global row
        row = row
        col = 0 # Initialize column
        

        # Retrieve guessed word from WordleGWindow
        guessed_word = gw.get_square_letter(row,0)+ gw.get_square_letter(row,1)+ gw.get_square_letter(row,2)+ gw.get_square_letter(row,3)+gw.get_square_letter(row,4)
        print(guessed_word) # For debugging

        # Check if player perfectly guessed the Wordle
        if guessed_word == Word:
            for x in range(0, N_COLS): # Iterate through all columns and color all squares green
                gw.set_square_color(WordleGWindow.get_current_row(gw), x, CORRECT_COLOR)
            gw.show_message("Winner winner chicken dinner!")
        else: # Player didn't perfectly guess the Wordle
            if guessed_word.lower() in FIVE_LETTER_WORDS: # If guessed word is a valid word
                while col < N_COLS : # Iterate through columns of guessed word
                    if guessed_word[col] == Word[col]: # If current column's letter in guessed word equals current column's letter in the Wordle
                        gw.set_square_color(row,col,color=CORRECT_COLOR)
                        gw.set_key_color(guessed_word[col],color=CORRECT_COLOR)
                        print("\"" + guessed_word[col] + "\" is correct")
                    elif guessed_word[col] in Word: # If current column's letter in guessed word is present somewhere in the Wordle
                        gw.set_square_color(row,col,color=PRESENT_COLOR)
                        gw.set_key_color(guessed_word[col],color=PRESENT_COLOR)
                        print("\"" + guessed_word[col] + "\" is somwhere in \"" + Word + "\"")
                    else: # Letter in guessed word is neither correct nor present in the Wordle
                        gw.set_square_color(row,col,color=MISSING_COLOR)
                        gw.set_key_color(guessed_word[col],color=MISSING_COLOR)
                        print("\"" + guessed_word[col] + "\" is not found in \"" + Word + "\"")
                    
                    col += 1 # Increment column number

                # Check if this was player's last guess
                if WordleGWindow.get_current_row(gw) == (N_ROWS - 1):
                    gw.show_message("You ran out of guesses! The Wordle was: \"" + Word + "\"")
                else:
                    # Show player how many guesses they have left
                    gw.show_message("Good guess! You have " + str((N_ROWS - 1) - row) + " guesses left.")
                    row += 1 # Increment row number
                    gw.set_current_row(row) # Continue to next row
                
            else: # Guessed word is invalid
                gw.show_message("\"" + guessed_word + "\" is not a real 5 letter word")
                # Row will stay the same here so that the player can backspace and enter a new word
        
    
        
    # #color change
    # def pick_colors(s):
        

    # Randomly choose the Wordle from the dictionary
    Word = random.choice(FIVE_LETTER_WORDS).upper()
    print(Word) # For debugging

    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()


    ## add anoyherchecker for hte key action
    ## unicaode charactosrs they are chiecking for, you can add another one or change it. 

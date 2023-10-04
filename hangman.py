import random
import time
import os
import sys

#Invite to the game

print("\n Welcome to Hangman! \n")
name = input("\n What is your name? \n")
print("Hello" + name + "!Good luck")
time.sleep(1)
print("Loading")
time.sleep(2)
print("The game is about to start!\n Let us play Hangman")
time.sleep(3)

#Parameters we require to execute:

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

words_list = ["march", "super", "splendin", "spiderman", "deathstroke", "chocolate", "heart", "happy", "toronto", "cairo", "warso", "paris", "chicago"]

word = random.choice(words_list)

length = len(word)
count = 0 #initially
display = '_' * length
already_guessed = []  #initially an empty list
play_game = ""

# Loop to re-execute the game when first attempt is done
def play_loop():
    global play_game
    play_game = input("Wanna play again? y=yes, n=no\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Wanna play again? y=yes, n=no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Bye! See you Later")
        exit()

# Initializing all conditions 

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    # Increase or decrease difficulty
    limit = 5
    guess = input("this is Hangman Word: " + display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("invalid input! try a letter, please! \n")
    elif guess in already_guessed:
        print("try another letter. \n")
    else:
        count+=1
        if count == 1:
            time.sleep(1)
            #drawing the shape manually
            print("  ----\n"
                  "  |     \n"
                  "  |     \n"   
                  "  |     \n"
                  "  |     \n"                 
                  "  |     \n"
                  "__|__\n")
            print("Wrong guess!" + str(limit - count))
        elif count == 2:
            time.sleep(1)
            print("  ----\n"
                  "  |      \n"
                  "  |      \n"   
                  "  |      \n"
                  "  |      \n"                 
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess!" + str(limit - count) + "remaining guesses!")
        elif count == 3:
            time.sleep(1)
            print("  -------\n"
                  "  |      \n"
                  "  |      \n"   
                  "  |      \n"
                  "  |      \n"                 
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess!" + str(limit - count) + "remaining guess!")
        elif count == 4:  
            time.sleep(1) 
            print("  ------\n"
                  "  |    |  \n"
                  "  |    |  \n"   
                  "  |    |  \n"
                  "  |    O  \n"                 
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess!" + str(limit - count) + "last remaining guess!")      
        else:
            time.sleep(1) 
            print("  ------\n"
                  "  |    |  \n"
                  "  |    |  \n"   
                  "  |    O  \n"
                  "  |   /|\  \n"                 
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess! You are hanged !!!  \n ")
            print("The word was:", already_guessed, word)
            play_loop()
 
    if word == "_" * length:
        print("Congrats!!! You are alive")
        play_loop()
    elif count != limit:
        hangman()

main()
hangman()












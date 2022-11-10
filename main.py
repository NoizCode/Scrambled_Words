import random
import os
import platform

clear = "clear"
main_loop = True

if platform.system() == "Windows":
    clear = "cls"

words = [
    "words",
    "programming",
    "speaker",
    "mousepad",
    "television",
    "book",
    "guitar",
    "chair",
    "apple",
    "bullet",
    "alien",
    "helmet",
    "guitar",
    "wardrobe",
    "smoke",
    "phone",
    "monitor",
    "music",
    "food",
    "wipe"
]

def scramble():
    global scrambled_word, letter

    while True:
        letter = random.choice(rand_word)
        if letter not in scrambled_word:
            scrambled_word += letter
        elif letter in scrambled_word and rand_word.count(letter) > 1:
            if rand_word.count(letter) != scrambled_word.count(letter):
                scrambled_word += letter
            else:
                continue

        if len(scrambled_word) == len(rand_word):
            break
        
    return scrambled_word

def check_win():
    if guess == rand_word:
        return 1
    else:
        return 0

while main_loop:
    os.system(clear)
    rand_word = random.choice(words)
    scrambled_word = ""
    letter = ""
    print("Word: ", end="")
    print(scramble())
    guess = input("Your guess: ")

    if check_win() == 1:
        print(f"\nCongratulations! You found the word: {rand_word}")
    else:
        print(f"\nWrong. The word is: {rand_word}")
    
    play = input("\nDo you want to play again?(y/n) ")
    if play == "y" or play == "Y":
        continue
    else:
        main_loop = False
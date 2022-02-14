import random
import os

def wordle_game():

    print("Ok let's play the wordle game!!!")

    with open(os.path.join("Games", "words.txt"), "r") as file:
            print(os.path.join("Games", "words.txt"))
            allText = file.read()
            word = random.choice(list(map(str, allText.split())))
    
    print(f'This is the secret word: {word}')
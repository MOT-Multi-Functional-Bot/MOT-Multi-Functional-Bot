import random

def wordle_game():

    print("Ok let's play the wordle game!!!")
    with open("Games\words.txt", "r") as file:
            allText = file.read()
            word = random.choice(list(map(str, allText.split())))
    
    print(f'This is the secret word: {word}')
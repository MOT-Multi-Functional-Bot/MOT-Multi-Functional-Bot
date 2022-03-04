import json
from games.wordle.exceptions import GuessEx, LoseEx, WinEx
from games.wordle.wordlist import check_if_word_exists, get_random_word


class Guess:
    def __init__(self, word: str, correction: str, correct_guess: bool = False):
        self.correct_guess = correct_guess  # if player hat guessed correct
        self.correction = correction  # progress for player
        self.word = word  # word that needs to be guessed


class wordle:
    def __init__(self):
        self.finished = False  # state of the game
        self.guesses = []  # guesses of the player
        self.progress = ["_"] * 5  # progress while guessing
        self.wrong_pos_letters = set()  # letters the player guessed right
        self.selected_word = get_random_word().upper()  # word that was selected for the player
        self.tries = 6  # amount of tries allowed
        self.wrong_letters = set()  # wrong letters guessed by player
        # For debugging purposes
        print("The Player needs to guess the word:", self.selected_word)

    def state(self) -> str:
        # Build the state of the game for the player
        msg = self.results()
        msg += "\n\n"
        msg += "Word:\n"
        msg += f"`{''.join(self.progress)}`"
        msg += "\n\n"
        msg += "Misplaced Letters:\n"
        msg += " ".join(sorted(self.wrong_pos_letters))
        msg += "\n\n"
        msg += "Wrong Letters:\n"
        msg += " ".join(sorted(self.wrong_letters))

        # check if game is finished -> display remaining tries
        if not self.finished:
            msg += "\n\n"
            msg += f"You have {self.tries} tries remaining!"

        return msg  # Current state of the game

    def solve_guess(self, guess_input: str) -> bool:
        formatted_word = ""
        # go through all letters of the word
        for pos, (current_letter, word_letter) in enumerate(
            zip(guess_input, self.selected_word)
        ):
            # if letter is not in the word at the current position
            if current_letter not in self.selected_word:
                formatted_word += "⬛"
                # add the letter to the list of wrong letters
                self.wrong_letters.add(current_letter)

            # if letter is in the word at the current position
            elif current_letter == word_letter:
                formatted_word += "🟩"
                # add the letter to the list of right letters
                self.progress[pos] = current_letter

            else:
                # amount of occurences of the current letter in the word
                letter_amount = self.selected_word.count(current_letter)
                # i = pos; l = letter
                for i, l in enumerate(self.selected_word):
                    # check if letter is the current letter
                    if l == current_letter:
                        # check if the playery guess includes the current letter
                        if guess_input[i] == current_letter:
                            # reduce letter amount
                            letter_amount -= 1

                # check if the letter amount is zero, add a fail
                if letter_amount == 0:
                    formatted_word += "⬛"

                else:
                    formatted_word += "🟪"
                    # add to list of letters at the wrong position
                    self.wrong_pos_letters.add(current_letter)

        # iterate through every letter
        for letter in (i for i in self.progress if i != "_"):
            # check if letter is in the wrong pos list
            if letter in self.wrong_pos_letters:
                # remove letter
                self.wrong_pos_letters.remove(letter)

        # add guess to the list guesses
        self.guesses.append(Guess(guess_input, formatted_word))

        # return the guess formatted for the ui
        return formatted_word

    def guess(self, guess: str, userid: str) -> Guess:
        # check if player input has the correct length
        if len(guess) != 5:
            raise GuessEx("The guesses word has the wrong amount of letters!")

        # check if player word exists in our wordlist
        if not check_if_word_exists(guess.lower()):
            raise GuessEx("The guessed word is not in the list of supported words!")

        # if word passes the tests above, count the try
        self.tries -= 1

        # get the formatted guess
        guess_corrected = self.solve_guess(guess)

        # check if the guess is correct; set all letters to correct if true
        is_guess_correct = guess_corrected == 5 * "🟩"

        # check if guess is correct
        if is_guess_correct:
            # set finish variable
            self.finished = True
            # raise exception to end the game

            # Save stats
            wordle.save_stats(self, userid)

            raise WinEx(f"You have successfully guess the word {self.selected_word}!")

        # check if there are tries left
        if self.tries == 0:
            # set finish variables and raise exception to end the game
            self.finished = True
            # Save stats
            wordle.save_stats(self, userid)
            # set tries to signal a lose
            self.tries = -1
            raise LoseEx(f"No more tries left. Your word was {self.selected_word}!")

        # return the guess from the player, formatted_word and a bool if the guess was correct
        return Guess(guess, guess_corrected, is_guess_correct)

    # top of the ui
    def results(self) -> str:
        # check if game finished before a lose
        if self.tries != -1:
            # calc the number of guesses needed
            guesses_needed = 6 - self.tries
        else:
            # player lost game
            guesses_needed = "X"

        msg = f"[{guesses_needed}/6]\n"
        msg += "\n"
        msg += "\n".join(guess.correction for guess in self.guesses)

        return msg

    def save_stats(self, userid):
        guesses_needed = 6 - self.tries
        # check if file exists
        try:
            f = open("games\wordle\stats.json", "r")
        # if file does not exist, create it
        except FileNotFoundError:
            print("Stats file count not be found, so it will be created!")
            f = open("games\wordle\stats.json", "w+")
            f.write("{}")
            f.close()
        # open stats file
        try:
            f = open("games\wordle\stats.json", "r")
            data = json.load(f)
            # create player if not existent
            if userid not in data:
                data[userid] = {}
                data[userid]["games_played"] = 0
                data[userid]["games_lost"] = 0
                data[userid]["games_won"] = 0
                data[userid]["guesses_1"] = 0
                data[userid]["guesses_2"] = 0
                data[userid]["guesses_3"] = 0
                data[userid]["guesses_4"] = 0
                data[userid]["guesses_5"] = 0
            # update player stats
            data[userid]["games_played"] += 1
            if guesses_needed < 6:
                data[userid]["games_won"] += 1
            if guesses_needed == 1:
                data[userid]["guesses_1"] += 1
            elif guesses_needed == 2:
                data[userid]["guesses_2"] += 1
            elif guesses_needed == 3:
                data[userid]["guesses_3"] += 1
            elif guesses_needed == 4:
                data[userid]["guesses_4"] += 1
            elif guesses_needed == 5:
                data[userid]["guesses_5"] += 1
            elif guesses_needed == 6:
                data[userid]["games_lost"] += 1
        except FileNotFoundError:
            print("Stats file count not be found!")
        finally:
            f.close()
            # save data to file
            with open("games\wordle\stats.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

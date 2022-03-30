from .exceptions import GuessEx, WinEx
import random


def get_random_number(x) -> int:
    return random.randrange(x)


class numtoguess:
    def __init__(self, numb: int, correct_guess: bool = False):
        self.numb = numb
        self.correct_guess = correct_guess


class numbergame:
    def __init__(self):
        self.finished = False
        self.selected_number = get_random_number(100)
        self.tries = 0
        self.reset = False
        self.newrange = 0
        # For debugging purposes
        # print("Number to guess: ", self.selected_number)

    def state(self) -> str:

        msg = self.results()
        if not self.finished:
            msg += "\n\n"
            msg += f"You have {self.tries} tries remaining!"

        return msg

    def numb(self, guess: str, userid: str) -> numtoguess:

        if self.reset:
            if not guess.isnumeric():
                raise GuessEx("The guess is not a number")

            if int(guess) > self.newrange or int(guess) < 0:
                raise GuessEx("Your number is out of range 0-100")
        else:
            if not guess.isnumeric():
                raise GuessEx("The guess is not a number")

            if int(guess) > 100 or int(guess) < 0:
                raise GuessEx(f"Your number is out of range 0-{self.newrange}")

        self.tries += 1

        is_guess_correct = int(guess) == self.selected_number

        if is_guess_correct:
            self.finished = True

            raise WinEx(f"You have successfully guess the word {self.selected_number}!")

        if int(guess) < self.selected_number:
            raise GuessEx(f"My number is bigger than: {guess}")

        if int(guess) > self.selected_number:
            raise GuessEx(f"My number is smaller than: {guess}")

        return numtoguess(guess, is_guess_correct)

    def newnum(self, guess: str, userid: str) -> numtoguess:

        if self.reset:
            raise GuessEx("You already did one reset! No more resets for you!")

        self.reset = True
        self.newrange = int(guess)

        if not guess.isnumeric():
            raise GuessEx("The new number is not a number")

        if int(guess) > 1000000 or int(guess) < 0:
            raise GuessEx("Your range is to big, the maximum is 1.000.000")

        self.tries = 0
        self.selected_number = get_random_number(int(guess))

        raise GuessEx(f"New number in range of 0-{int(guess)} was set.")

    def results(self) -> str:

        msg = "Well, you got me. o.O \n"
        msg += "It only took you " + str(self.tries) + " tries! Damn!"

        return msg

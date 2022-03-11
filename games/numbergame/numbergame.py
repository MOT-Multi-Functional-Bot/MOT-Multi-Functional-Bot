import random
from games.numbergame.exceptions import GuessEx, WinEx


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
        print("Number of Computer: ", self.selected_number)

    def state(self) -> str:

        msg = self.results()
        if not self.finished:
            msg += "\n\n"
            msg += f"You have {self.tries} tries remaining!"

        return msg

    def numb(self, guess: str, userid: str) -> numtoguess:

        if self.reset:
            if not guess.isnumeric():
                raise GuessEx("the guess is not a number")

            if int(guess) > self.newrange or int(guess) < 0:
                raise GuessEx("Your number is out of range 0-100")
        else:
            if not guess.isnumeric():
                raise GuessEx("the guess is not a number")

            if int(guess) > 100 or int(guess) < 0:
                raise GuessEx(f"Your number is out of range 0-{self.newrange}")

        self.tries += 1

        is_guess_correct = int(guess) == self.selected_number
        print(
            f"guess: {int(guess)} ist gleich set: {self.selected_number} oder: {int(guess) == self.selected_number}"
        )

        if is_guess_correct:
            self.finished = True

            print("ich raise win")
            raise WinEx(f"You have successfully guess the word {self.selected_number}!")

        if int(guess) < self.selected_number:
            raise GuessEx(f"My number is bigger than: {guess}")

        if int(guess) > self.selected_number:
            raise GuessEx(f"My number is smaller than: {guess}")

        return numtoguess(guess, is_guess_correct)

    def newnum(self, guess: str, userid: str) -> numtoguess:

        if self.reset:
            raise GuessEx("You already did one reset no more for you!")

        self.reset = True
        self.newrange = int(guess)

        if not guess.isnumeric():
            raise GuessEx("The nw Number is not a Number")

        if int(guess) > 1000000 or int(guess) < 0:
            raise GuessEx("Your Range is to Big, max 1.000.000")

        self.tries = 0

        print(f"Old num: {self.selected_number} New range: {int(guess)}")
        self.selected_number = get_random_number(int(guess))
        print(f"New num: {self.selected_number}")

        raise GuessEx(f"New number in range of 0-{int(guess)} was set.")

    def results(self) -> str:

        msg = "\n"
        msg += "Hilfe du hast mich ertappt. o.O"
        msg += "\n"
        msg += "und das nur mit "
        msg += f"{self.tries}"
        msg += " Versuchen. Krass!"

        return msg

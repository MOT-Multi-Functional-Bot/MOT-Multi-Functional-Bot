#!/usr/bin/env python
import random
from telegram import Update
from main_commands import send_message
from TicTacToe.exceptions import WinEx, LoseEx, GuessEx


class Guess:
    def __init__(self, input):
        self.input

class TicTacToe_Game:

    def __init__(self) -> None:
        self.randomNumber = random.randint(1, 99)
        random.seed(self.randomNumber)


        self.gCache = {}
        self.gPlayers = [0, 1]
        self.gStart = 0
        self.gAllLines = [
                self.set_bits([0, 1, 2]),
                self.set_bits([3, 4, 5]),
                self.set_bits([6, 7, 8]),
                self.set_bits([0, 3, 6]),
                self.set_bits([1, 4, 7]),
                self.set_bits([2, 5, 8]),
                self.set_bits([0, 4, 8]),
                self.set_bits([2, 4, 6]),
                ]



    def guess(self, guess: str) -> Guess:
        # check if player input has the correct length
        if len(guess) != 5:
            raise GuessEx("The guesses word has the wrong amount of letters!")

        # check if player word exists in our wordlist
        

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
            raise WinEx(f"You have successfully guess the word {self.selected_word}!")

        # check if there are tries left
        if self.tries == 0:
            # set finish variables and raise exception to end the game
            self.finished = True
            # set tries to signal a lose
            self.tries = -1
            raise LoseEx(f"No more tries left. Your word was {self.selected_word}!")

        # return the guess from the player, formatted_word and a bool if the guess was correct
        return Guess(guess, guess_corrected, is_guess_correct)




    def set_bits(self, Bits):
        result = 0
        for b in Bits:
            result |= 1 << b
        return result


    def set_bit(n):
        return 1 << n


    def to_board(self, state):
        result = ''
        for cell in range(9):
            if state & (2 ** cell) != 0:
                result += '✖'
            elif state & (2 ** (cell + 9)) != 0:
                result += '⭕'
            else:
                result += '⬜'
            if (cell + 1) % 3 == 0:
                result += '\n'
        return result


    def empty(self, state):
        Free = {n for n in range(9)}
        Free -= {n for n in range(9) if state & (1 << n) != 0}
        Free -= {n for n in range(9) if state & (1 << (9 + n)) != 0}
        return Free

    def next_states(self, state, player):
        Empty = self.empty(state)
        Result = []
        for n in Empty:
            next_state = state | self.set_bit(player * 9 + n)
            Result.append(next_state)
        return Result


    def utility(self, state):
        for mask in self.gAllLines:
            if state & mask == mask:
                return 1
            if (state >> 9) & mask == mask:
                return -1

        if (state & 511) | (state >> 9) != 511:
            return None

        return 0


    def finished(self, state):
        return self.utility(state) != None


    def get_move(self, state, update: Update):
        while True:
            try:
                row, col = input('Bitte Zug eingeben: ').split(',')
                row, col = int(row), int(col)
                if row not in {0, 1, 2} or col not in {0, 1, 2}:
                    send_message( update, 'Illegale Eingabe. Die Eingabe muss die Form "Zeile, Spalte" haben')  
                    send_message( update, 'where row and col are numbers from the set {0,1,2}.')
                    continue
                mask = self.set_bit(row * 3 + col)
                if state & (mask | (mask << 9)) == 0:
                    return state | (mask << 9)
                send_message( update, "Don't cheat! Versuchts nochmal.")
            except:
                send_message( update, 'Illegale Eingabe.')  
                send_message( update, 'Zeile und Spalte sind elemente der Menge {0,1,2}.')



    def final_msg(self, state, update: Update):
        if self.finished(state):
            if self.utility(state) == -1:
                send_message( update, 'Du hast gewonnen!')
            elif self.utility(state) == 1:
                send_message( update, 'Der Computer hat gewonnen')
            else:
                send_message( update, "Unendschieden")
            return True
        return False


    size = 150


    def get_symbol(self, state, row, col):
        mask = self.set_bit(row * 3 + col)
        if mask & state == mask:
            return 'X'
        if mask & (state >> 9) == mask:
            return 'O'
        return ' '


    def draw(self, state):
        x = self.to_board(state)
        # print(x)
        return x


    def evaluate(self, State, f, alpha=-1, beta=1):
        global gCache
        if State in gCache:
            flag, v = gCache[State]
            if flag == '=':
                return v
            if flag == '≤':
                if v <= alpha:
                    return v
                elif alpha < v < beta:
                    w = f(State, alpha, v)
                    self.store_cache(State, alpha, v, w)
                    return w
                else:
                    w = f(State, alpha, beta)
                    self.store_cache(State, alpha, beta, w)
                    return w
            if flag == '≥':
                if beta <= v:
                    return v
                elif alpha < v < beta:
                    w = f(State, v, beta)
                    self.store_cache(State, v, beta, w)
                    return w
                else:
                    w = f(State, alpha, beta)
                    self.store_cache(State, alpha, beta, w)
                    return w
        else:
            v = f(State, alpha, beta)
            self.store_cache(State, alpha, beta, v)
            return v


    def store_cache(self, State, alpha, beta, v):
        global gCache
        if v <= alpha:
            gCache[State] = ('≤', v)
        elif v < beta:
            gCache[State] = ('=', v)
        else:
            gCache[State] = ('≥', v)


    def maxValue(self, State, alpha, beta):
        if self.finished(State):
            return self.utility(State)
        if alpha >= beta:
            return alpha
        v = alpha
        for ns in self.next_states(State, self.gPlayers[0]):
            v = max(v, self.evaluate(ns, self.minValue, v, beta))
            if v >= beta:
                return v
        return v


    def minValue(self, State, alpha, beta):
        if self.finished(State):
            return self.utility(State)
        if beta <= alpha:
            return beta
        v = beta
        for ns in self.next_states(State, self.gPlayers[1]):
            v = min(v, self.evaluate(ns, self.maxValue, alpha, v))
            if v <= alpha:
                return v
        return v


    def best_move(self, State):
        NS = self.next_states(State, self.gPlayers[0])
        bestValue = self.evaluate(State, self.maxValue, -1, 1)
        BestMoves = [s for s in NS if self.evaluate(s, self.minValue, -1, 1) == bestValue]
        BestState = random.choice(BestMoves)
        return bestValue, BestState


    def main(self, state, update, context) -> None:
        State = self.gStart
        while (True):
            val, State = self.best_move(State)
            x = self.draw(State)
            #print(x)
            send_message( update, x)
            if self.finished(State):
                self.final_msg(State, update)
                break
            State = self.get_move(State, update)
            x = self.draw(State)
            #print(x)
            send_message( update, x)
            if self.finished(State):
                self.final_msg(State, update)
                break
    

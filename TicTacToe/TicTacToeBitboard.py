#!/usr/bin/env python
from sre_parse import State
import string
from IPython.display import display, display_svg
from TicTacToe.exceptions import WinEx, LoseEx, GuessEx
import random

class Guess:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

global msg, state, update
msg = "TEST"


class ticTac:
    print("TicAufgerufen !!!!")
    def __init__(self) -> None:
        global State
        self.gPlayers = [0, 1]
        self.gStart = 0
        self.gCache = {}
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
        self.State = self.gStart
        self.randomNumber = random.randint(1, 99)
        random.seed(self.randomNumber)


    def guess(self, row: int, col: int) -> Guess:
        print("guess")
        return Guess(row, col)



    def evaluate(self, f, alpha=-1, beta=1):
        print("evaluate")
        global gCache, State
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


    def store_cache(self, alpha, beta, v):
        global State
        print("StoreCache")
        global gCache
        if v <= alpha:
            gCache[State] = ('≤', v)
        elif v < beta:
            gCache[State] = ('=', v)
        else:
            gCache[State] = ('≥', v)


    def maxValue(self, State, alpha, beta):
        print("Maxval")
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
        print("minVal")
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


    def best_move(self):
        global State
        print("best_move")
        NS = self.next_states(State, self.gPlayers[0])
        bestValue = self.evaluate(State, self.maxValue, -1, 1)
        BestMoves = [s for s in NS if self.evaluate(s, self.minValue, -1, 1) == bestValue]
        BestState = random.choice(BestMoves)
        return bestValue, BestState


    def set_bits(self, Bits):
        print("set_bits")
        result = 0
        for b in Bits:
            result |= 1 << b
        return result


    def set_bit(n):
        print("set_bit")
        return 1 << n


    def to_board(self) -> string:
        global State
        print("toBoard")
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


    def empty(self):
        global State
        print("empty")
        Free = {n for n in range(9)}
        Free -= {n for n in range(9) if state & (1 << n) != 0}
        Free -= {n for n in range(9) if state & (1 << (9 + n)) != 0}
        return Free


    def next_states(self, player):
        global State
        print("next_states")
        Empty = self.empty(state)
        Result = []
        for n in Empty:
            next_state = state | self.set_bit(player * 9 + n)
            Result.append(next_state)
        return Result


    def utility(self):
        global State
        print("utility")
        for mask in self.gAllLines:
            if state & mask == mask:
                return 1
            if (state >> 9) & mask == mask:
                return -1

        if (state & 511) | (state >> 9) != 511:
            return None

        return 0


    def finished(self):
        global State
        print("finished")
        return self.utility(state) != None


    def get_move(self):
        global State, update
        print("get_Move")
        while True:
            try:
                row, col = input('Move eingeben bitte: ').split(',')
                row, col = int(row), int(col)
                mask = self.set_bit(9 + row * 3 + col)
                if state & mask == 0:
                    return state | mask
                update.message.reply_text("Nicht cheaten.")
            except:
                update.message.reply_text('Illegaler Input.')
                update.message.reply_text(
                    'Reihen und Zeilen sind Elemente aus: {0,1,2}.')


    def final_msg(self):
        global State, update
        print("final_msg")
        if self.finished(state):
            if self.utility(state) == -1:
                update.message.reply_text('Du hast gewonnen!')
            elif self.utility(state) == 1:
                update.message.reply_text('Der Computer hat gewonnen')
            else:
                update.message.reply_text("Unendschieden")
            return True
        return False

    def get_symbol(self, row, col):
        global State
        print("get_Symbol")
        mask = self.set_bit(row * 3 + col)
        if mask & state == mask:
            return 'X'
        if mask & (state >> 9) == mask:
            return 'O'
        return ' '


    def draw(self) -> str:
        global State
        print("draw")

        x = self.to_board(state)
        print(x)
        return x


    def state(self) -> str:
        self.gamexyz()
        return msg

    def gamexyz(self) -> None:
        print("MAINMAINMAINMAIN")
        global msg, State, update
        State = self.gStart
    
        _, State = self.best_move(State)
        msg = self.draw(State) # -> String
        state(self.x)
        # update.message.reply_text(x) # !
        if self.finished(State):
            self.final_msg(State, update)
            # break
        State = self.guess()
        print(f'State = {State}')
        msg = self.draw(State)  # -> String
        state(self.x)
        # update.message.reply_text(x) # !
        if self.finished(State):
            self.final_msg(State, update)
            # break

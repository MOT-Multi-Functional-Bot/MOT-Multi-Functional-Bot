#!/usr/bin/env python
import random
randomNumber = random.randint(1, 99)
random.seed(randomNumber)


gCache = {}
gPlayers = [0, 1]
gStart = 0


def set_bits(Bits):
    result = 0
    for b in Bits:
        result |= 1 << b
    return result


def set_bit(n):
    return 1 << n


def to_board(state):
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


def empty(state):
    Free = {n for n in range(9)}
    Free -= {n for n in range(9) if state & (1 << n) != 0}
    Free -= {n for n in range(9) if state & (1 << (9 + n)) != 0}
    return Free


state = set_bits([2, 3, 5, 9+1, 9+4, 9+8])
empty(state)


def next_states(state, player):
    Empty = empty(state)
    Result = []
    for n in Empty:
        next_state = state | set_bit(player * 9 + n)
        Result.append(next_state)
    return Result


gAllLines = [set_bits([0, 1, 2]),
             set_bits([3, 4, 5]),
             set_bits([6, 7, 8]),
             set_bits([0, 3, 6]),
             set_bits([1, 4, 7]),
             set_bits([2, 5, 8]),
             set_bits([0, 4, 8]),
             set_bits([2, 4, 6]),
             ]


def utility(state):
    for mask in gAllLines:
        if state & mask == mask:
            return 1
        if (state >> 9) & mask == mask:
            return -1

    if (state & 511) | (state >> 9) != 511:
        return None

    return 0


def finished(state):
    return utility(state) != None


def get_move(state, update):
    while True:
        try:
            row, col = input('Bitte Zug eingeben: ').split(',')
            row, col = int(row), int(col)
            if row not in {0, 1, 2} or col not in {0, 1, 2}:
                update.message.reply_text('Illegale Eingabe. Die Eingabe muss die Form "Zeile, Spalte" haben')  
                update.message.reply_text('where row and col are numbers from the set {0,1,2}.')
                continue
            mask = set_bit(row * 3 + col)
            if state & (mask | (mask << 9)) == 0:
                return state | (mask << 9)
            update.message.reply_text("Don't cheat! Versuchts nochmal.")
        except:
            update.message.reply_text('Illegale Eingabe.')  
            update.message.reply_text('Zeile und Spalte sind elemente der Menge {0,1,2}.')



def final_msg(state, update):
    if finished(state):
        if utility(state) == -1:
            update.message.reply_text('Du hast gewonnen!')
        elif utility(state) == 1:
            update.message.reply_text('Der Computer hat gewonnen')
        else:
            update.message.reply_text("Unendschieden")
        return True
    return False


size = 150


def get_symbol(state, row, col):
    mask = set_bit(row * 3 + col)
    if mask & state == mask:
        return 'X'
    if mask & (state >> 9) == mask:
        return 'O'
    return ' '


def draw(state):
    x = to_board(state)
    # print(x)
    return x


def evaluate(State, f, alpha=-1, beta=1):
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
                store_cache(State, alpha, v, w)
                return w
            else:
                w = f(State, alpha, beta)
                store_cache(State, alpha, beta, w)
                return w
        if flag == '≥':
            if beta <= v:
                return v
            elif alpha < v < beta:
                w = f(State, v, beta)
                store_cache(State, v, beta, w)
                return w
            else:
                w = f(State, alpha, beta)
                store_cache(State, alpha, beta, w)
                return w
    else:
        v = f(State, alpha, beta)
        store_cache(State, alpha, beta, v)
        return v


def store_cache(State, alpha, beta, v):
    global gCache
    if v <= alpha:
        gCache[State] = ('≤', v)
    elif v < beta:
        gCache[State] = ('=', v)
    else:
        gCache[State] = ('≥', v)


def maxValue(State, alpha, beta):
    if finished(State):
        return utility(State)
    if alpha >= beta:
        return alpha
    v = alpha
    for ns in next_states(State, gPlayers[0]):
        v = max(v, evaluate(ns, minValue, v, beta))
        if v >= beta:
            return v
    return v


def minValue(State, alpha, beta):
    if finished(State):
        return utility(State)
    if beta <= alpha:
        return beta
    v = beta
    for ns in next_states(State, gPlayers[1]):
        v = min(v, evaluate(ns, maxValue, alpha, v))
        if v <= alpha:
            return v
    return v


def best_move(State):
    NS = next_states(State, gPlayers[0])
    bestValue = evaluate(State, maxValue, -1, 1)
    BestMoves = [s for s in NS if evaluate(s, minValue, -1, 1) == bestValue]
    BestState = random.choice(BestMoves)
    return bestValue, BestState


def main(state, update, context) -> None:
    State = gStart
    while (True):
        val, State = best_move(State)
        x = draw(State)
        #print(x)
        update.message.reply_text(x)
        if finished(State):
            final_msg(State, update)
            break
        State = get_move(State, update)
        x = draw(State)
        #print(x)
        update.message.reply_text(x)
        if finished(State):
            final_msg(State, update)
            break
    

if __name__ == '__main__':
    print(gStart)
    main(gStart, update, CallbackContext)

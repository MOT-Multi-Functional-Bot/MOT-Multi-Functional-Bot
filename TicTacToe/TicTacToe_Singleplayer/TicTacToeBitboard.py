#!/usr/bin/env python
from IPython.display import display, display_svg


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
            row, col = input('Move einfeben bitte: ').split(',')
            row, col = int(row), int(col)
            mask = set_bit(9 + row * 3 + col)
            if state & mask == 0:
                return state | mask
            update.message.reply_text("Nicht cheaten.")
        except:
            update.message.reply_text('Illegaler Input.')
            update.message.reply_text(
                'Reihen und Zeilen sind Elemente aus: {0,1,2}.')


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

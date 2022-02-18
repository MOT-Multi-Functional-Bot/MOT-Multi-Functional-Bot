
gPlayers = [0, 1]
gStart = 0

def set_bits(Bits):
    result = 0
    for b in Bits:
        result |= 1 << b # bitwise or 2**b
    return result

"{:b}".format(set_bits([0, 1, 4]))

assert set_bits([0, 1, 4]) == 2**0 + 2**1 + 2**4

def set_bit(n): 
    return 1 << n

assert set_bit(7) == 2 ** 7

def to_board(state):
    result = '+-+-+-+\n'
    for cell in range(9):
        if state & (2 ** cell) != 0:
            result += '|X'
        elif state & (2 ** (cell + 9)) != 0:
            result += '|O'
        else:
            result += '| '
        if (cell + 1) % 3 == 0:
            result += '|\n+-+-+-+\n'
    return result

def empty(state):
    Free  = { n for n in range(9) }
    Free -= { n for n in range(9) if state & (1 << n) != 0 }
    Free -= { n for n in range(9) if state & (1 << (9 + n)) != 0 }
    return Free

state = set_bits([2, 3, 5, 9+1, 9+4, 9+8])
print(to_board(state))
empty(state)

def next_states(state, player):
    Empty  = empty(state)
    Result = []
    for n in Empty:
        next_state = state | set_bit(player * 9 + n)
        Result.append(next_state)
    return Result

state = set_bits([2,3,5,10,13,15])
print(f'state:\n{to_board(state)}')
print('next states:')                  
for s in next_states(state, 0):
    print(to_board(s))

gAllLines = [ set_bits([0,1,2]), # 1st row
              set_bits([3,4,5]), # 2nd row
              set_bits([6,7,8]), # 3rd row
              set_bits([0,3,6]), # 1st column
              set_bits([1,4,7]), # 2nd column
              set_bits([2,5,8]), # 3rd column
              set_bits([0,4,8]), # falling diagonal
              set_bits([2,4,6]), # rising diagonal
            ]

for state in gAllLines:
    print(to_board(state))

def utility(state):
    for mask in gAllLines:
        if state & mask == mask:
            return 1               # the computer has won
        if (state >> 9) & mask == mask:
            return -1              # the computer has lost
    # 511 == 2**9 - 1 = 0b1_1111_1111  
    if (state & 511) | (state >> 9) != 511: # the board is not yet filled
        return None
    # at this point, the board has been filled, but there is no winner hence its a draw
    return 0 # it's a draw

s1 = set_bits([0, 2, 3, 6, 1+9,  4+9, 5+9]) # 'X' has won
print(to_board(s1))
utility(s1)

s2 = set_bits([0, 2, 6, 8, 1+9, 4+9, 7+9]) # 'O' has won
print(to_board(s2))
utility(s2)

s3 = set_bits([0, 2, 5, 6, 7, 1+9, 3+9, 4+9, 8+9]) # it's a draw
print(to_board(s3))
print(utility(s3))

s4 = set_bits([0, 2, 5, 6, 1+9, 3+9, 4+9]) # it ain't over yet
print(to_board(s4))
print(utility(s4))

def finished(state): 
    return utility(state) != None

s = set_bits([0, 2, 5, 6, 7, 1+9, 3+9, 4+9, 8+9])
print(to_board(s))
finished(s)

def get_move(state):
    while True:
        try:
            row, col = input('Enter move here: ').split(',')
            row, col = int(row), int(col)
            mask = set_bit(9 + row * 3 + col)
            if state & mask == 0:
                return state | mask
            print("Don't cheat! Please try again.")
        except:
            print('Illegal input.')  
            print('row and col are numbers from the set {0,1,2}.')

def final_msg(state):
    if finished(state):
        if utility(state) == -1:
            print('You have won!')
        elif utility(state) == 1:
            print('The computer has won!')
        else:
            print("It's a draw.");
        return True
    return False

import ipycanvas as cnv

size = 150

def create_canvas():
    canvas = cnv.Canvas(size=(size * 3, size * 3 + 50))
    display(canvas)
    return canvas


def get_symbol(state, row, col):
    mask = set_bit(row * 3 + col)
    if mask & state == mask:
        return 'X'
    if mask & (state >> 9) == mask:
        return 'O'
    return ' '  

def draw(state, canvas, value):
    canvas.clear()
    n = 3
    canvas.font          = '90px sans-serif'
    canvas.text_align    = 'center'
    canvas.text_baseline = 'middle'
    for row in range(n):
        for col in range(n):
            x = col * size
            y = row * size
            canvas.line_width = 3.0
            canvas.stroke_rect(x, y, size, size)
            symbol = get_symbol(state, row, col)
            if symbol != ' ':
                x += size // 2
                y += size // 2
                if symbol == 'X':
                    canvas.fill_style ='red'
                else:
                    canvas.fill_style ='blue'
                canvas.fill_text(symbol, x, y)
    canvas.font = '12px sans-serif'
    canvas.fill_style = 'green'
    for row in range(n):
        for col in range(n):
            x = col * size + 16
            y = row * size + 141
            canvas.fill_text(f'({row}, {col})', x, y)
    canvas.font = '20px sans-serif'
    canvas.fill_style = 'black'
    x = 1.5 * size
    y = 3.2 * size
    canvas.fill_text(str(value), x, y)

draw(set_bits([0, 2, 5, 6, 1+9, 3+9, 4+9]), create_canvas(), -1)
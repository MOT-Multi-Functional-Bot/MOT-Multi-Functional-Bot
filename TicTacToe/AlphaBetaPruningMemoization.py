#!/usr/bin/env python


import IPython.display
from TicTacToeBitboard import *

from IPython.core.display import HTML


import random
randomNumber = random.randint(1,99)
random.seed(randomNumber)


gCache = {}


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



len(gCache)


def best_move(State):
    NS = next_states(State, gPlayers[0])
    bestValue = evaluate(State, maxValue, -1, 1)
    BestMoves = [s for s in NS if evaluate(s, minValue, -1, 1) == bestValue]
    BestState = random.choice(BestMoves)
    return bestValue, BestState


def play_game(state):
    State = gStart
    while (True):
        val, State = best_move(State)
        draw(State)
        if finished(State):
            final_msg(State)
            break
        State = get_move(State)
        draw(State)
        if finished(State):
            final_msg(State)
            break


draw(gStart)

play_game(gStart)

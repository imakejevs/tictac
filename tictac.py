#!/bin/python

import random

# how to mark cells on battlefield
empty = 0 
player = 1
me = 2

game = [[empty, empty, empty],          # battlefield
        [empty, empty, empty],
        [empty, empty, empty]]

heatmap = [[0, 0, 0, 0, 0, 0, 0, 0],    # player
           [0, 0, 0, 0, 0, 0, 0, 0]]    # me
max_heat = [-3,-3]

# True=my turn, False=human's turn
turn = False

# print board
def print_board():
    print "  1 2 3"
    for row in range(3):
        print("{0} {1} {2} {3}".format(row+1, p(game[row][0]), p(game[row][1]), p(game[row][2])))

# return cell mark
def p(val):
    if val == player:
        return 'X'
    if val == me:
        return 'O'
    return '.'

# do we have a winner?
def check_win(x):
    for row in range(3):
        if game[row][0] == x and game[row][1] == x and game[row][2] == x:
            return True
    for col in range(3):
        if game[0][col] == x and game[1][col] == x and game[2][col] == x:
            return True
    if game[0][0] == x and game[1][1] == x and game[2][2] == x:
        return True
    if game[2][0] == x and game[1][1] == x and game[0][2] == x:
        return True
    return False

# our turn
def our_turn():
    global heatmap
    for side in [player,me]:
        for i in range(1,9):
            heatmap[side - 1][i - 1] = check(i,side)
            if check(i,side) > max_heat[side - 1]:
                max_heat[side - 1] = i

    print("X:{0} O:{1}".format(max_heat[0],max_heat[1]))

    for side in [player,me]:
        add_our(max_heat[side - 1])

    if turn:
            add_our(random.randint(1,8))

# how many cells in row,col,diag
def check(x,who):
# return number of X or O in a row, col or diag
# 1 2 3 - rows
# 4 5 6 - cols
# 7 - \
# 8 - /
    num = 0

    if x >= 1 and x <= 3:
        for col in range(3):
            if game[x - 1][col] == who:
                num += 1
            else:
                num -= 1

    if x >= 4 and x <= 6:
        for row in  range(3):
            if game[row][x - 4] == who:
                num += 1
            else:
                num -= 1

    if x == 7:
        for i in range(3):
            if game[i][i] == who:
                num += 1
            else:
                num -= 1
        
    if x == 8:
        for i in range(3):
            if game[2-i][i] == who:
                num += 1
            else:
                num -= 1

    # print("[{0}] {1} {2}".format(x,p(who),num))
    return num
        

# add our mark on board during our turn for cell,row,diag
def add_our(x):
# adds O to a row, col or diag, same as for check(x)
    if x >= 1 and x <= 3:
        for col in range(3):
            if game[x - 1][col] == empty:
                add(x - 1, col)

    if x >= 4 and x <= 6:
        for row in  range(3):
            if game[row][x - 4] == empty:
                add(row, x - 4)

    if x == 7:
        if game[0][0] == empty:
            add(0,0)
        if game[1][1] == empty:
            add(1,1)
        if game[2][2] == empty:
            add(2,2)

    if x == 8:
        if game[2][0] == empty:
            add(2,0)
        if game[1][1] == empty:
            add(1,1)
        if game[0][2] == empty:
            add(0,2)    

# add mark at row,col
def add(row, col):
    global turn
    if turn:
        if game[row][col] == empty:
            game[row][col] = me
            turn = False

# main loop
while(True):
    if check_win(player):
        print_board()
        print "You win!"
        exit()

    if turn:
        our_turn()
        if check_win(me):
            print_board()
            print "I win!"
            exit()
    else:
        print_board()
        str = raw_input("enter row col: ")
        inp = str.split(' ')
        row = int(inp[0])
        col = int(inp[1])
        if game[row - 1][col - 1] == empty:
            game[row - 1][col - 1] = player
            turn = True
            print "  "


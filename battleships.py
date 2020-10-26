

import os
import sys
import string
from art import *
import numpy as np
import random as r
from time import sleep


empty = "."

ship_hits = {"A":0, "B":0, "C":0, "D":0}
hit_tracker = {"A":[], "B":[], "C":[], "D":[]}
cols = list(string.ascii_uppercase)[0:10]
player_board = np.array([[empty]*10]*10)
enemy_board = np.array([[empty]*10]*10)
ships = {"A":5, "B":4, "C":4, "D":3}
miss_counter = 0
hit_counter = 0
locations = []
noftorp = 0


def place_check(c, sign, x, y, ship_num, locations):
    x_check = x
    y_check = y
    overlap = False

    if c == 'x':
        for i in range(ship_num):
            x_check += sign
            if [x_check, y] in locations:
                overlap = True
    else:
        for i in range(ship_num):
            y_check += sign
            if [x, y_check] in locations:
                overlap = True

    return(overlap)


def restart():
    global cols ,player_board ,ships ,miss_counter ,hit_counter ,locations, noftorp, empty, ship_hits, enemy_board

    ship_hits = {"A":0, "B":0, "C":0, "D":0}
    hit_tracker = {"A":[], "B":[], "C":[], "D":[]}
    cols = list(string.ascii_uppercase)[0:10]
    player_board = np.array([[empty]*10]*10)
    enemy_board = np.array([[empty]*10]*10)
    ships = {"A":5, "B":4, "C":4, "D":3}
    miss_counter = 0
    hit_counter = 0
    locations = []
    noftorp = 0

    for i in ships.items():
        ship_id = i[0]
        i = i[1]
        row_location = r.randint(0, 8)
        column_location = r.randint(0, 8)

        x = column_location
        y = row_location

        xl = []
        yl = []

        for j in range(i):
            row_dir = 1
            col_dir = 1

            if row_location > (i-1):
                if column_location < i:
                    if j == 0:
                        while(True):
                            overlap = place_check('x', 1, x, y, i, locations)
                            if not overlap:
                                break
                            else:
                                y += row_dir
                                if y > 9:
                                    y = 0

                    x += col_dir
                    locations.append([x, y])

                    enemy_board[y, x] = ship_id
                    xl.append(x)
                    yl.append(y)
                    continue
                else:
                    if j == 0:
                        while(True):
                            overlap = place_check('x', -1, x, y, i, locations)
                            if not overlap:
                                break
                            else:
                                y -= row_dir
                                if y < 0:
                                    y = 9

                    x -= col_dir
                    locations.append([x, y])

                    enemy_board[y, x] = ship_id
                    xl.append(x)
                    yl.append(y)
                    continue

            else:
                if j == 0:
                    while(True):
                        overlap = place_check('y', 1, x, y, i, locations)
                        if not overlap:
                            break
                        else:
                            x += col_dir
                            if x > 9:
                                x = 0

                y += row_dir
                locations.append([x, y])

                enemy_board[y, x] = ship_id
                xl.append(x)
                yl.append(y)
                continue

            if column_location > (i-1):
                if j == 0:
                    while(True):
                        overlap = place_check('y', 1, x, y, i, locations)
                        if not overlap:
                            break
                        else:
                            x += col_dir
                            if x > 9:
                                x = 0

                y += row_dir
                locations.append([x, y])

                enemy_board[y, x] = ship_id
                xl.append(x)
                yl.append(y)
                continue

            else:
                if j == 0:
                    while(True):
                        overlap = place_check('y', 1, x, y, i, locations)
                        if not overlap:
                            break
                        else:
                            x += col_dir
                            if x > 9:
                                x = 0

                y += row_dir
                locations.append([x, y])

                enemy_board[y, x] = ship_id
                xl.append(x)
                yl.append(y)
                continue


def inc_message(msg):
    inc = ("Incoming Message")
    msg_start = False

    os.system("cls")

    tprint("\n\n\n\n")

    for part in msg:
        for nn, ch in enumerate(part):
            if nn == 0 and not msg_start:
                msg_start = True
                sys.stdout.write(inc)
                sys.stdout.flush()
                sleep(0.05)

            if nn == 1:
                sys.stdout.write(ch)
                sys.stdout.flush()
                sleep(1)

            elif nn > 1:
                sys.stdout.write(ch)
                sys.stdout.flush()
                sleep(0.05)
        sleep(1.5)
    

def print_board():
    global player_board
    global miss_counter
    global hit_counter
    global empty
    global enemy_board

    os.system("cls")

    print()
    print("="*32)
    print("PLAYER STATS:")
    print("="*32)
    print("Hits: {}\nMisses: {}\n".format(hit_counter, miss_counter))
    cols = list(string.ascii_uppercase)[0:10]
    print(" "*5, end="")
    for i in cols:
        print(i, " "*2, end="")

    print("\n   " + "-"*40) # Top boarder

    for n, i in enumerate(player_board):
        if (n + 1) < 10:
            print((n+1), " | ", end="")
        else:
            print((n+1), "| ", end="")
        for j in i:
            print(j, " "*2, end="")
        print()
        print("   | ")
    print()


def start():
    global player_board
    global hit_counter
    global miss_counter
    global noftorp

    restart()

    while(True):
        print_board()

        #print(enemy_board) # This shows the actual location of all enemy ships

        rst = False
        skip = False

        row_guess = 0
        col_guess = 0

        print("\n* Enter 'r' To Restart")
        print("""
* Enter Coordinates Like This:  a1
                                b5
                                a7\n""")

        while(True):
            try:
                col_guess = input("Enter Coordinates To Fire On: ").upper()

                if col_guess == "R":
                    os.system("cls")
                    print("Restarting...")
                    sleep(1)
                    rst = True
                    break

                if len(col_guess) > 1:
                    if len(col_guess) > 2:
                        c_guess = (col_guess[0]).upper()
                        c_guess = cols.index(c_guess)
                        r_guess = ''.join(col_guess[1:])
                        r_guess = int(r_guess)

                        col_guess = c_guess
                        row_guess = (r_guess - 1)

                        skip = True
                        break
                    else:
                        c_guess = (col_guess[0]).upper()
                        c_guess = cols.index(c_guess)
                        r_guess = int(col_guess[1])

                        col_guess = c_guess
                        row_guess = (r_guess - 1)

                        skip = True
                        break

                col_guess = cols.index(col_guess)
                break
            except:
                print("Please enter a letter between A and J")

        while(True):
            if rst or skip:
                skip = False
                break
            try:
                row_guess = input("Row (1-10): ")

                if row_guess == "R" or row_guess == "r":
                    os.system("cls")
                    print("Restarting...")
                    sleep(1)
                    rst = True
                    break

                row_guess = (int(row_guess) - 1)
                if row_guess >= 0 and row_guess <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10")
            except:
                print("Please enter a number between 1 and 10")

        if rst:
            restart()
            continue

        shot = enemy_board[row_guess, col_guess]
        
        if shot != empty:
            player_board[row_guess, col_guess] = 'X'
            ship_hits[shot] += 1
            hit_tracker[shot].append([row_guess, col_guess])
            if ship_hits[shot] >= ships[shot]:
                for i in hit_tracker[shot]:
                    player_board[i[0], i[1]] = '*'

                msg = " : ENEMY UNIT [{}] HAS BEEN SUNK!".format(shot)
                inc_message([msg])

            hit_counter += 1
            noftorp += 1
        
        else:
            player_board[row_guess, col_guess] = 'O'
            miss_counter += 1
            noftorp += 1

        if hit_counter >= 16:
            msg1 = " : I'm sorry major, there is no one left..."
            msg2 = "  You killed them all! ;)"
            msg = [msg1, msg2]
            inc_message(msg)

            again = (input("\n\n\nPlay Again (y|n)? ")).lower()
            if 'n' in again:
                break
            else:
                restart()


start()

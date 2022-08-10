import random

from exception import trigger_exception
from desk import Desk
from player import PlayerHuman, PlayerAI
# initialization
player_1 = PlayerHuman()
player_2 = PlayerAI()
desk_1 = Desk()
desk_2 = Desk()
player_1.init_desk(desk_1)
player_2.init_desk(desk_2)

k = 0
num = 0
delta = 0
flag = 0  # for AI: if it caught ship - it will continue check the environment if this cell
move_2 = 0

rand_sequence = [i * 10 + j for j in range(1, 7) for i in range(1, 7)]  # for AI
tumbler = random.choice([1, 2])  # the choice of the first move: 1 - human player, 2 - AI
if tumbler == 1:
    print("Your move is the first")
else:
    print("Your rival's move is the first")
while desk_1.get_list_of_ships() and desk_2.get_list_of_ships():
    if tumbler == 1:  # the move of human player
        print("Your rival's desk:")
        desk_1.print_field(2)
        index = input("Take a move (2-digit number) on rival's field: ")
        try:
            trigger_exception(index)
        except ValueError:
            print("Index isn't a number or is out of range")
            continue
        else:
            move_1 = int(index)
            if move_1 in player_1.get_moves():
                print("You have already tried this move, try again")
                continue
            else:
                player_1.add_move(move_1)
                s = desk_2.check_move(move_1)
                if s == "case 1":  # case with bad shot
                    print("Bad shot! Transition to rival")
                    desk_1.add_move(move_1, 1)
                    tumbler = 2
                elif s == "case 2":  # case with ship getting caught
                    print("Ship is got caught")
                    desk_1.add_move(move_1, 2)
                    continue
                elif s == "case 3":  # case with ship destroy, draw contour of ship
                    print("Ship is destroyed")
                    desk_1.add_move(move_1, 2)
                    num = desk_2.get_number()
                    contour = desk_2.get_contour(num)
                    desk_1.draw_contour(contour)
                    continue
    if tumbler == 2:  # the move of AI player
        if flag == 0:
            move_2 = random.choice(rand_sequence)
        else:  # if ship is got caught
            if k == 2:  # searching for 3rd cell of 3-cell ship
                if abs(ind2 - ind1) == 1:
                    delta = random.choice([-10, -9, -1, 2, 10, 11])
                    move_2 = min(ind1, ind2) + delta
                else:
                    delta = random.choice([-10, -1, 1, 9, 11, 20])
                    move_2 = min(ind1, ind2) + delta
            else:  # searching for the 2nd cell of 2-cell and 3-cell ship
                delta = random.choice([1, -1, 10, -10])
                move_2 += delta
        if move_2 not in rand_sequence:
            move_2 -= delta
            continue
        else:
            player_2.add_move(move_2)
            rand_sequence.remove(move_2)
            s = desk_1.check_move(move_2)
            if s == "case 1":
                desk_2.add_move(move_2, 1)
                tumbler = 1
                move_2 -= delta
                print("Rival missed out")
            elif s == "case 2":
                desk_2.add_move(move_2, 2)
                flag = 1
                num = desk_1.get_number()
                if num == 1 and k == 0:  # 1st cell of 3-cell ship is caught
                    ind1 = move_2
                    k += 1
                elif num == 1 and k == 1:  # 2nd cell of 3-cell ship is caught
                    ind2 = move_2
                    k += 1
                print("Rival caught your ship!")
                desk_1.print_field(1)
                continue
            elif s == "case 3":  # ship is destroyed, eliminate contour from range of indexes
                desk_2.add_move(move_2, 2)
                flag = 0
                num = desk_1.get_number()
                contour = desk_1.get_contour(num)
                if num == 1:  # we destroyed 3-cell ship
                    k = 0
                rand_sequence = [i for i in rand_sequence if i not in contour]
                print("Rival destroyed your ship!")
                desk_1.print_field(1)
                continue

if desk_1.get_list_of_ships():
    print("You win!")
elif desk_2.get_list_of_ships():
    print("The winner is AI..")

import random

from exception import trigger_exception, NotNumber, OutOfRange

class Game:
    def __init__(self, player1, desk1, player2, desk2):
        self.rand_sequence = [i * 10 + j for j in range(1, 7) for i in range(1, 7)]  # for AI
        self.flag = 0  # if AI caught ship - it will continue check the environment of this cell
        self.k = 0
        self.tumbler = 1
        self.move_2 = 0
        self.ind1 = 0
        self.ind2 = 0
        self.player_1 = player1
        self.desk_1 = desk1
        self.player_2 = player2
        self.desk_2 = desk2

    def human_move(self):
        while self.desk_1.get_list_of_ships() and self.desk_2.get_list_of_ships():
            print("Your rival's desk:")
            self.desk_1.print_field(2)
            index = input("Take a move (2-digit number) on rival's field: ")
            try:
                trigger_exception(index)
            except NotNumber:
                print(f"{index} is a string")
                continue
            except OutOfRange:
                print(f"{index} is out of range")
                continue
            else:
                move_1 = int(index)
                if move_1 in self.player_1.get_moves():
                    print("This move have already been used, try again")
                    continue
                else:
                    self.player_1.add_move(move_1)
                    s = self.desk_2.check_move(move_1)
                    if s == "case 1":  # case with bad shot
                        print("Bad shot! Transition to rival")
                        self.desk_1.add_move(move_1, 1)
                        break
                    elif s == "case 2":  # case with ship getting caught
                        print("Ship is got caught")
                        self.desk_1.add_move(move_1, 2)
                        continue
                    elif s == "case 3":  # case with ship destroy, draw contour of ship
                        print("Ship is destroyed")
                        self.desk_1.add_move(move_1, 2)
                        num = self.desk_2.get_number()
                        contour = self.desk_2.get_contour(num)
                        self.desk_1.draw_contour(contour)
                        continue
        self.tumbler += 1
        return True

    def ai_move(self):
        while self.desk_1.get_list_of_ships() and self.desk_2.get_list_of_ships():
            if self.flag == 0:
                self.move_2 = random.choice(self.rand_sequence)
                delta = 0
            else:  # if ship is got caught
                if self.k == 2:  # searching for 3rd cell of 3-cell ship
                    if abs(self.ind2 - self.ind1) == 1:
                        delta = random.choice([-10, -9, -1, 2, 10, 11])
                        self.move_2 = min(self.ind1, self.ind2) + delta
                    else:
                        delta = random.choice([-10, -1, 1, 9, 11, 20])
                        self.move_2 = min(self.ind1, self.ind2) + delta
                else:  # searching for the 2nd cell of 2-cell and 3-cell ship
                    delta = random.choice([1, -1, 10, -10])
                    self.move_2 += delta
            if self.move_2 not in self.rand_sequence:
                self.move_2 -= delta
                continue
            else:
                self.player_2.add_move(self.move_2)
                self.rand_sequence.remove(self.move_2)
                s = self.desk_1.check_move(self.move_2)
                if s == "case 1":
                    self.desk_2.add_move(self.move_2, 1)
                    self.move_2 -= delta
                    print("AI missed out. The current state of your desk:")
                    self.desk_1.print_field(1)
                    break
                elif s == "case 2":
                    self.desk_2.add_move(self.move_2, 2)
                    self.flag = 1
                    num = self.desk_1.get_number()
                    if num == 1 and self.k == 0:  # 1st cell of 3-cell ship is caught
                        self.ind1 = self.move_2
                        self.k += 1
                    elif num == 1 and self.k == 1:  # 2nd cell of 3-cell ship is caught
                        self.ind2 = self.move_2
                        self.k += 1
                    print("AI caught your ship! The current state of your desk after his move:")
                    self.desk_1.print_field(1)
                    continue
                elif s == "case 3":  # ship is destroyed, eliminate contour from range of indexes
                    self.desk_2.add_move(self.move_2, 2)
                    self.flag = 0
                    num = self.desk_1.get_number()
                    contour = self.desk_1.get_contour(num)
                    if num == 1:  # we destroyed 3-cell ship
                        self.k = 0
                    self.rand_sequence = [i for i in self.rand_sequence if i not in contour]
                    print("AI destroyed your ship! The current state of your desk after his move:")
                    self.desk_1.print_field(1)
                    continue
        self.tumbler += 1
        return True

    def game_cycle(self):
        self.tumbler = random.choice([1, 2])  # the choice of the first move: 1 - human player, 2 - AI
        if self.tumbler % 2 == 1:
            print("Your move is the first")
        elif self.tumbler % 2 == 0:
            print("The first move belongs to AI")
        while self.desk_1.get_list_of_ships() and self.desk_2.get_list_of_ships():
            if self.tumbler % 2 == 1:
                self.human_move()
            if self.tumbler % 2 == 0:
                self.ai_move()

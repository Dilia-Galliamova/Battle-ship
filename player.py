import random

from exception import trigger_exception
from ship import Ship


class PlayerHuman:
    def __init__(self):
        self.moves = []

    def get_moves(self):
        return self.moves

    def add_move(self, index):
        self.moves.append(index)

    def init_desk(self, desk):
        count = 1
        k = 1
        print("Please follow the instruction to enter ship indexes one by one. Index is a 2-digit number (for example 11, 12 etc.)")
        while count != 8:
            if count < 2:  # creating of 3-cell ship
                s = input(f"Input {k} index for 3-cell ship OR R to reset desk and start again: ")
                if s == "R":
                    desk.reset_desk()
                    count = 1
                    k = 1
                    continue
                try:
                    trigger_exception(s)
                except ValueError:
                    print("Index isn't a number or out of range")
                    continue
                else:
                    if k == 1:  # the 1st index
                        x = int(s)
                        k += 1
                        continue
                    elif k == 2:  # the 2nd index
                        y = int(s)
                        k += 1
                        continue
                    elif k == 3:  # the 3rd index
                        z = int(s)
                        ship = Ship(sorted([x, y, z]), 3)
                        if ship.check_connection():
                            desk.add_and_draw_ship(ship, count)
                            count += 1
                            k = 1
                            desk.print_field(1)
                        else:
                            print("Indexes aren't neighbours, try again")
                            k = 1
            if 1 < count < 4:  # 2-cell ships
                s = input(f"Input {k} index for {count - 1} 2-cell ship OR R to reset desk and start again: ")
                if s == "R":
                    desk.reset_desk()
                    count = 1
                    k = 1
                    continue
                try:
                    trigger_exception(s)
                except ValueError:
                    print("Index isn't a number or out of range")
                    continue
                else:
                    if k == 1:  # the 1st index
                        x = int(s)
                        k += 1
                        continue
                    elif k == 2:  # the 2nd index
                        y = int(s)
                        ship = Ship(sorted([x, y]), 2)
                        if ship.check_connection():
                            if desk.check_index(ship) is False:
                                print("There are intersections with other ships, try again")
                                k = 1
                                continue
                            else:
                                desk.add_and_draw_ship(ship, count)
                                k = 1
                                count += 1
                                desk.print_field(1)
                        else:
                            print("Indexes aren't neighbours, try again")
                            k = 1
            if 3 < count < 8:  # 1-cell ships
                s = input(f"Input index for {count - 3} 1-cell ship OR R to reset desk and start again: ")
                if s == "R":
                    desk.reset_desk()
                    count = 1
                    k = 1
                    continue
                try:
                    trigger_exception(s)
                except ValueError:
                    print("Index isn't a number or out of range")
                    continue
                else:
                    x = int(s)
                    ship = Ship(x, 1)
                    if desk.check_index(ship) is False:
                        print("There are intersections with other ships, try again")
                        continue
                    else:
                        desk.add_and_draw_ship(ship, count)
                        count += 1
                        desk.print_field(1)


class PlayerAI:
    def __init__(self):
        self.moves = []

    def get_moves(self):
        return self.moves

    def add_move(self, index):
        self.moves.append(index)

    def init_desk(self, desk):
        count = 1
        k = 1
        rand_sequence = [i * 10 + j for j in range(1, 7) for i in range(1, 7)]
        while count != 8:
            if k > 100:
                desk.reset_desk()
                k = 1
                count = 1
            if count < 2:
                x = random.choice(rand_sequence)
                y = x + random.choice([1, -1, 10, -10])
                try:
                    trigger_exception(y)
                except ValueError:
                    k += 1
                    continue
                else:
                    z = y + random.choice([1, -1, 10, -10])
                    try:
                        trigger_exception(z)
                    except ValueError:
                        k += 1
                    else:
                        if x == z:
                            k += 1
                            continue
                        else:
                            ship = Ship(sorted([x, y, z]), 3)
                            desk.add_and_draw_ship(ship, count)
                            count += 1
            if 1 < count < 4:
                x = random.choice(rand_sequence)
                y = x + random.choice([1, -1, 10, -10])
                try:
                    trigger_exception(y)
                except ValueError:
                    k += 1
                    continue
                else:
                    ship = Ship(sorted([x, y]), 2)
                    if desk.check_index(ship) is False:
                        k += 1
                        continue
                    else:
                        desk.add_and_draw_ship(ship, count)
                        count += 1
            if 3 < count < 8:
                x = random.choice(rand_sequence)
                ship = Ship(x, 1)
                if desk.check_index(ship) is False:
                    k += 1
                    continue
                else:
                    desk.add_and_draw_ship(ship, count)
                    count += 1

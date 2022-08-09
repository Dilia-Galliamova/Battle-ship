class Desk:
    def __init__(self):
        self.own_field = [["o"] * 8 for i in range(8)]
        self.rival_field = [["o"] * 8 for i in range(8)]
        self.list_of_ships = {}
        self.ship_contour = {}
        self.number = 0

    def reset_desk(self):
        self.own_field = [["o"] * 8 for i in range(8)]
        self.list_of_ships = {}

    def get_contour(self, number):
        return self.ship_contour[number]

    def get_number(self):
        return self.number

    def get_list_of_ships(self):
        return self.list_of_ships

    def add_move(self, move, tumbler):  # draw the result of move on rival field
        i = move // 10
        j = move % 10
        if tumbler == 1:
            self.rival_field[i][j] = "T"
        elif tumbler == 2:
            self.rival_field[i][j] = "x"

    def draw_contour(self, contour):  # draw dots on rival field in case of ship destroy
        for item in contour:
            i = item // 10
            j = item % 10
            if self.rival_field[i][j] == "o":
                self.rival_field[i][j] = "."

    def print_field(self, tumbler):
        if tumbler == 1:  # print own field
            print("  1 2 3 4 5 6")
            for i in range(1, 7):
                print(i, end=" ")
                for j in range(1, 7):
                    print(self.own_field[i][j], end=" ")
                print()
        elif tumbler == 2:  # print rival field
            print("  1 2 3 4 5 6")
            for i in range(1, 7):
                print(i, end=" ")
                for j in range(1, 7):
                    print(self.rival_field[i][j], end=" ")
                print()

    def add_and_draw_ship(self, ship, count):  # draw ship on field during initialization
        self.list_of_ships[count] = ship
        if ship.get_size() == 1:
            i = ship.get_index() // 10
            j = ship.get_index() % 10
            self.own_field[i][j] = "*"
            contour = []
            for x in range(i - 1, i + 2):  # create contour of ship
                for y in range(j - 1, j + 2):
                    contour.append(x * 10 + y)
            contour.remove(ship.get_index())
            self.ship_contour[count] = contour
        elif ship.get_size() == 2:
            for cnt in range(2):
                i = ship.get_index()[cnt] // 10
                j = ship.get_index()[cnt] % 10
                self.own_field[i][j] = "*"
            ind1 = ship.get_index()[0]  # part with getting contour of ship
            ind2 = ship.get_index()[1]
            buf = []
            i1 = ind1 // 10
            j1 = ind1 % 10
            for x in range(i1 - 1, i1 + 2):
                for y in range(j1 - 1, j1 + 2):
                    buf.append(x * 10 + y)
            i2 = ind2 // 10
            j2 = ind2 % 10
            for x in range(i2 - 1, i2 + 2):
                for y in range(j2 - 1, j2 + 2):
                    buf.append(x * 10 + y)
            contour = []
            for item in buf:
                if item not in contour:
                    contour.append(item)
            contour = [i for i in contour if i not in ship.get_index()]
            self.ship_contour[count] = contour
        elif ship.get_size() == 3:
            for cnt in range(3):  # draw ship
                i = ship.get_index()[cnt] // 10
                j = ship.get_index()[cnt] % 10
                self.own_field[i][j] = "*"
            ind1 = ship.get_index()[0]  # part with getting contour of ship
            ind2 = ship.get_index()[1]
            ind3 = ship.get_index()[2]
            buf = []
            i1 = ind1 // 10
            j1 = ind1 % 10
            for x in range(i1 - 1, i1 + 2):
                for y in range(j1 - 1, j1 + 2):
                    buf.append(x * 10 + y)
            i2 = ind2 // 10
            j2 = ind2 % 10
            for x in range(i2 - 1, i2 + 2):
                for y in range(j2 - 1, j2 + 2):
                    buf.append(x * 10 + y)
            i3 = ind3 // 10
            j3 = ind3 % 10
            for x in range(i3 - 1, i3 + 2):
                for y in range(j3 - 1, j3 + 2):
                    buf.append(x * 10 + y)
            contour = []
            for item in buf:
                if item not in contour:
                    contour.append(item)
            contour = [i for i in contour if i not in ship.get_index()]
            self.ship_contour[count] = contour

    def check_index(self, ship):  # check if we can draw ship. 3-cell ship is setting first, we don't check it
        if ship.get_size() == 1:
            i = ship.get_index() // 10
            j = ship.get_index() % 10
            for x in range(i - 1, i + 2):  # check the environment for case of intersection
                for y in range(j - 1, j + 2):
                    if self.own_field[x][y] != "o":
                        return False
        if ship.get_size() == 2:
            ind1 = ship.get_index()[0]
            ind2 = ship.get_index()[1]
            if (ind2 - ind1) == 1:  # case with horizontal ship
                i = ship.get_index()[0] // 10
                j = ship.get_index()[0] % 10
                for x in range(i - 1, i + 2):  # check the environment for case of intersection
                    for y in range(j - 1, j + 3):
                        if self.own_field[x][y] != "o":
                            return False
            elif (ind2 - ind1) == 10:  # case with vertical ship
                i = ship.get_index()[0] // 10
                j = ship.get_index()[0] % 10
                for x in range(i - 1, i + 3):  # check the environment for case of intersection
                    for y in range(j - 1, j + 2):
                        if self.own_field[x][y] != "o":
                            return False

    def check_move(self, move):
        i = move // 10
        j = move % 10
        if self.own_field[i][j] == "o":  # bad shot
            return "case 1"
        elif self.own_field[i][j] == "*":
            self.own_field[i][j] = "x"
            cnt_new = 0
            for cnt, char in self.list_of_ships.items():  # getting number of ship, that we caught
                if self.list_of_ships[cnt].get_size() == 1:
                    if move == self.list_of_ships[cnt].get_index():
                        cnt_new = cnt
                else:
                    if move in self.list_of_ships[cnt].get_index():
                        cnt_new = cnt
            self.number = cnt_new
            size = self.list_of_ships[cnt_new].get_size()
            if size == 1:  # 1-cell ship is destroyed
                self.list_of_ships.pop(cnt_new)  # elimination from list
                return "case 3"
            else:
                count = 0
                for item in range(size):  # check if there is other living cells of ship
                    i = self.list_of_ships[cnt_new].get_index()[item] // 10
                    j = self.list_of_ships[cnt_new].get_index()[item] % 10
                    if self.own_field[i][j] == "*":
                        count += 1
                if count == 0:  # ship is destroyed
                    self.list_of_ships.pop(cnt_new)
                    return "case 3"
                else:  # ship is caught
                    return "case 2"

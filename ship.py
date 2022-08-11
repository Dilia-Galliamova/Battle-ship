class Ship:
    def __init__(self, index=0, size=0):
        self.size = size
        self.index = index

    def get_index(self):
        return self.index

    def get_size(self):
        return self.size

    def check_connection(self):  # check if input cells aren't connected
        if self.size == 2:
            x = self.index[0]
            y = self.index[1]
            if x == y:
                print("Indexes can't be repeated, try again")
                return False
            else:
                if (y - x) in [0, 1, 10]:
                    return True
                else:
                    print("Indexes aren't neighbours, try again")
                    return False
        elif self.size == 3:
            x = self.index[0]
            y = self.index[1]
            z = self.index[2]
            if x == y or y == z or x == z:
                print("Indexes can't be repeated, try again")
                return False
            else:
                if (y - x) in [0, 1, 9, 10] and (z - y) in [0, 1, 9, 10] and (z - x) in [0, 2, 10, 11, 20]:
                    return True
                else:
                    print("Indexes aren't neighbours, try again")
                    return False

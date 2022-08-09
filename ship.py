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
            if (y - x) in [0, 1, 10]:
                return True
            else:
                return False
        elif self.size == 3:
            x = self.index[0]
            y = self.index[1]
            z = self.index[2]
            if (y - x) in [0, 1, 9, 10] and (z - y) in [0, 1, 9, 10] and (z - x) in [0, 2, 10, 11, 20]:
                return True
            else:
                return False

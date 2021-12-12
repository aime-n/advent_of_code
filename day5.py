import numpy as np

n1 = 9
n2 = 7
n1 > n2
list(range(n1, n2-1, -1))


class Hypodrothermal():

    def __init__(self, shape):
        self.diagram = np.full(shape, '.')

    def set_range(n1, n2):
        if n2 > n1:
            return list(range(n1, n2+1))
        elif n2 < n1:
            return list(range(n1, n2-1, -1))

    def set_point(self, x, y):
        if self.diagram[x][y] == '.':
            self.diagram[x][y] = 1
        if int(self.diagram[x][y]) == int:
            self.diagram[x][y] += 1

    def set_coord(self, coord):
        x1, y1 = coord[0][0], coord[0][1]
        x2, y2 = coord[1][0], coord[1][1]
        if x1 == x2:
            range_y = Hypodrothermal.set_range(y1, y2)
            for y in range_y:
                Hypodrothermal.set_point(self, x1, y)
        elif y1 == y2:
            range_x = Hypodrothermal.set_range(x1, x2)
            for x in range_x:
                Hypodrothermal.set_point(self, x, y1)

    def __str__(self):
        str = ''
        for line in self.diagram:
            for point in line:
                str += point
            str += '\n'
        return f'{str}'


def test():
    with open('day5test.txt') as f:
        file = f.readlines()
    coord = []
    for line in file:
        first, second = line.split('->')
        first = tuple(map(int, first.split(',')))
        second = tuple(map(int, second.split(',')))
        coord.append((first, second))
    return coord


txt = test()
temp = Hypodrothermal((10, 10))
print(temp)


for i in txt:
    temp.set_coord(i)
print(temp)

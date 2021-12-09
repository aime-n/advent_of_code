txt = 'day1data.txt'

# part one

with open(txt) as f:
    lines = f.readlines()

list = [int(i) for i in lines]


def count_increases(list):
    c = 0
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            c += 1
    return c


count_increases(list)

# part two

c = 0
temp = [sum(list[i:i+3]) for i in range(0, len(list))]

count_increases(temp)

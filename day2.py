# Part One

'''

    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.


'''

txt = 'data2.txt'
with open(txt) as f:
    moves = f.readlines()

horizontal = 0
depth = 0

for move in moves:
    command, units = move.split()

    if command == 'forward':
        horizontal += int(units)
    elif command == 'down':
        depth += int(units)
    elif command == 'up':
        depth -= int(units)

print(horizontal * depth)

# Part Two

'''

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.


'''

aim = 0
depth = 0
horizontal = 0

for move in moves:
    command, units = move.split()
    if command == 'down':
        aim += int(units)
    if command == 'up':
        aim -= int(units)
    if command == 'forward':
        horizontal += int(units)
        depth += aim* int(units)

print(horizontal * depth)

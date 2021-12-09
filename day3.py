'''

gamma = most common bit in the corresponding position of all numbers
    the gamma rate is the binary number 10110, or 22 in decimal.

epsilon = the least common bit from each position

The power consumption can then be found by multiplying the gamma rate
by the epsilon rate, both in decimal.


'''

txt = "day3_data.txt"

with open(txt) as f:
    report = f.readlines()

print(report)

report_l = []
for line in report:
    temp = [int(i) for i in line[:-1]]
    report_l.append(temp)

sum = [sum(i) for i in zip(*report_l)]
print(sum)
print(len(report_l))

gamma, epsilon = '', ''

for number in sum:
    if number > 500:  # most common = 1
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

power = gamma * epsilon
print(power)

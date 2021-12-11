'''

gamma = most common bit in the corresponding position of all numbers
    the gamma rate is the binary number 10110, or 22 in decimal.

epsilon = the least common bit from each position

The power consumption can then be found by multiplying the gamma rate
by the epsilon rate, both in decimal.


'''

import numpy as np
txt = "day3_data.txt"

with open(txt) as f:
    file = f.readlines()


def file_to_matrix(file):
    matrix = []
    for line in file:
        temp = [int(i) for i in line[:-1]]
        matrix.append(temp)
    return matrix


def common_values(matrix):  # returns list
    sums = [sum(line) for line in zip(*matrix)]
    values = []
    for i in sums:
        if i > (len(matrix)/2):
            values.append(1)
        else:
            values.append(0)
    return values


def gamma_epsilon(values):
    gamma, epsilon = '', ''
    for i in values:
        if i == 0:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2), int(epsilon, 2)


report_matrix = file_to_matrix(file)
gamma, epsilon = gamma_epsilon(common_values(report_matrix))

power = gamma * epsilon
print(power)


'''

life support rating = oxygen generator rating * CO2 scrubber rating

oxygen generator rating = find most common value (0 or 1) in the bit
    position


'''


def find_oxygen(matrix):
    for i in range(matrix.shape[1]):
        sum_ = np.sum(matrix[:, i])
        if sum_ >= matrix.shape[0]/2:
            common = 1
        else:
            common = 0
        index_to_delete = []
        for j in range(matrix.shape[0]):
            if matrix[j][i] != common:
                index_to_delete.append(j)
        matrix = np.delete(matrix, index_to_delete, axis=0)
        if matrix.shape[0] == 1:
            return list_to_decimal(matrix[0])
    return list_to_decimal(matrix[0])

def find_CO2(matrix):
    for i in range(matrix.shape[1]):
        sum_ = np.sum(matrix[:, i])
        if sum_ >= matrix.shape[0]/2:
            least_common = 0
        else:
            least_common = 1
        index_to_delete = []
        for j in range(matrix.shape[0]):
            if matrix[j][i] != least_common:
                # print(f'{matrix[j][i]} diferente de {least_common}: {matrix[j]}')
                index_to_delete.append(j)
        matrix = np.delete(matrix, index_to_delete, axis=0)
        if matrix.shape[0] == 1:
            return list_to_decimal(matrix[0])
    return list_to_decimal(matrix[0])


def list_to_decimal(list):
    decimal = ''
    for i in list:
        decimal += str(i)
    return int(decimal, 2)


report_matrix = file_to_matrix(file)
report_matrix = np.array(report_matrix, dtype=int)
print(report_matrix)

oxygen = find_oxygen(report_matrix)
CO2 = find_CO2(report_matrix)
print(oxygen * CO2)

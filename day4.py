import numpy as np

# Part one: first winner


class Board:
    def __init__(self, board):
        self.board = board
        self.marked = np.full((5, 5), False, dtype=bool)
        self.n = None

    def mark_number(self, number):
        index = np.where(self.board == number)
        self.marked[index[0], index[1]] = True

    def check_winner(self):
        for i in range(5):
            column = self.marked[:, i]
            row = self.marked[i]
            if np.all(row):
                return True
            elif np.all(column):
                return True
        return False


def file_to_ndraws_boards(file):
    n_draw = list(map(int, file[0].split(',')))

    temp = []
    for i in range(1, len(file), 6):
        temp.append(file[i+1:i+6])

    boards = []
    for board in temp:
        board_ = []
        for row in board:
            board_.append([int(x) for x in row.split()])

        boards.append(Board(np.array(board_)))

    return n_draw, boards


def win_first(n_draw, boards):
    for n in n_draw:
        for board in boards:
            board.mark_number(n)
            if board.check_winner():
                return n, board


def score(n_winner, board_winner):
    index_false = np.where(board_winner.marked == False)
    to_sum = board_winner.board[index_false]
    return np.sum(to_sum) * n_winner


with open('day4.txt') as f:
    file = f.readlines()

n_draw, boards = file_to_ndraws_boards(file)
n_winner, board_winner = win_first(n_draw, boards)
print(score(n_winner, board_winner))


# Part two: last winner


def test():
    with open('day4test.txt') as f:
        file = f.readlines()

    n_draw, boards = file_to_ndraws_boards(file)
    return n_draw, boards


def win_last(n_draw, boards):
    winners = []
    for i in range(len(n_draw)):
        for board in boards:
            if board not in winners:
                board.mark_number(n_draw[i])
                if board.check_winner():
                    board.n = n_draw[i]
                    winners.append(board)
    return winners[-1]


n_draw, boards = test()
last = win_last(n_draw, boards)
print(last.marked)
print(last.n)

score(last.n, last)


n_draw, boards = file_to_ndraws_boards(file)
last = win_last(n_draw, boards)
print(score(last.n, last))

def find_square(index):
    return [[i, j] for i in range(index[0] - (index[0]%3), index[0] - (index[0]%3) + 3) for j in range(index[1] - (index[1]%3), index[1] - (index[1]%3) + 3)]

def find_possible_places(board, number):
    place = []
    for i in range(9):
        if number not in board[i]:
            for j in range(9):
                if board[i][j] == 0 and (number not in [board[n][j] for n in range(9)]) and (number not in [board[n[0]][n[1]] for n in find_square([i, j])]):
                    place.append([i, j])
    for square in [find_square([i, j]) for i in [0, 3, 6] for j in [0, 3, 6]]:
        inSquare = [i for i in place if i in square]
        if len(set([i[0] for i in inSquare])) == 1:
            place = [i for i in place if ((i[0] != inSquare[0][0]) or (i in inSquare))]
        elif len(set([i[1] for i in inSquare])) == 1:
            place = [i for i in place if ((i[1] != inSquare[0][1]) or (i in inSquare))]
    return place

def findNumbers(board, pos):
    inX = board[pos[0]]
    inY = [board[i][pos[1]] for i in range(9)]
    inSquare = [board[i][j] for [i, j] in find_square([pos[0], pos[1]])]
    return set(range(1, 10)) - set(inX + inY + inSquare)

def find_solutions(board, pos, num):
    possible_x = [pos[i][0] for i in range(len(pos))]
    possible_y = [pos[i][1] for i in range(len(pos))]
    change = True
    while change:
        change = False
        i = 0
        while i < len(pos):
            if possible_x.count(pos[i][0]) == 1:
                board[pos[i][0]][pos[i][1]] = num
                pos = find_possible_places(board, num)
                change = True
            elif possible_y.count(pos[i][1]) == 1:
                board[pos[i][0]][pos[i][1]] = num
                pos = find_possible_places(board, num)
                change = True
            elif len([p for p in pos if p in find_square([pos[i][0], pos[i][1]])]) == 1:
                board[pos[i][0]][pos[i][1]] = num
                pos = find_possible_places(board, num)
                change = True
            elif len(findNumbers(board, [pos[i][0], pos[i][1]])) == 1:
                board[pos[i][0]][pos[i][1]] = num
                pos = find_possible_places(board, num)
                change = True
            else:
                i = i + 1
    if len(pos) == 1:
        board[pos[0][0]][pos[0][1]] = num
        pos = []
    return board

def checker(board):
    for i in range(1, 10):
        for c in board:
            if c.count(i) != 1:
                return "Nope"
        for k in range(9):
            if [board[k][l] for l in range(9)].count(i) != 1:
                return "Nope"
        for s in [[i, j] for i in [0, 3, 6] for j in [0, 3, 6]]:
            if [board[c[0]][c[1]] for c in find_square(s)].count(i) != 1:
                return "Nope"
    return "YAY"

sudoku = [
    [0,6,0,4,0,0,0,7,0],
    [0,8,0,0,0,0,0,2,9],
    [0,7,0,0,2,0,5,0,0],
    [0,0,5,6,0,0,0,0,4],
    [9,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,3],
    [0,0,4,1,0,0,0,0,0],
    [8,0,0,0,9,0,0,0,0],
    [0,0,0,0,8,0,1,0,6]
]

ones = 0
zeros = sum([sudoku[i].count(0) for i in range(9)])

while zeros != ones:
    for i in range(1, 10):
        possible = find_possible_places(sudoku, i)
        if possible:
            sudoku = find_solutions(sudoku, possible, i)
    ones = zeros
    zeros = sum([sudoku[i].count(0) for i in range(9)])

for i in sudoku:
    print(i)

print(checker(sudoku))


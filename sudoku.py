bo = [
    [6,0,9,7,5,1,0,0,0],
    [0,0,0,0,0,3,0,0,4],
    [0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,8,0,0],
    [0,0,8,0,6,7,0,0,0],
    [0,0,0,0,0,9,1,5,6],
    [1,5,0,2,0,0,4,0,0],
    [0,0,0,0,0,0,0,0,5],
    [7,0,0,0,0,0,0,6,0]
]

def printBoard(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
            	print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def findZeros(board):

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return [y,x]

    return None

def checkConditions(board, val, loc):

    for i in range(len(board[0])):
        if board[loc[0]][i] == val and  i != loc[1]:
            return False

    for j in range(len(board)):
        if board[j][loc[1]] == val and j != loc[0]:
            return False

    box_x = loc[1] // 3
    box_y = loc[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 +3):
            if board[i][j] == val and [i,j] != [loc[0],loc[1]]:
                return False

    return True

def solver(board):

    find = findZeros(board)
    if not find:
        return True
    else:
        loc = find
    for i in range(1,10):
        if checkConditions(board, i, loc):
            board[loc[0]][loc[1]] = i
            if solver(board):
                return True
            board[loc[0]][loc[1]] = 0
    return False

def main():

	printBoard(bo)
	solver(bo)
	print('\n')
	print('Solved Sudoku Board:')
	print('\n')
	printBoard(bo)


main()
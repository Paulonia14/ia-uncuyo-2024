def create_empty_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)
    return board

def h_function(queens): #Contar ataques
    attacks = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            # Ataque horizontal
            if queens[i][0] == queens[j][0]:
                attacks += 1
            # Ataque vertical
            if queens[i][1] == queens[j][1]:
                attacks += 1
            # Ataque diagonal
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                attacks += 1
    return attacks

def CSP_backtracking(size):
    board = create_empty_board(size)
    cantqueens = size
    queens = []
    while cantqueens > 0:
        i = size - 1
        for j in range(size):
            print("i ",i)
            print("j ", j)
            queens.append((i, j))
            if h_function(queens) == 0:
                board[i][j] = 1
                cantqueens -= 1
            else:
                queens.pop()
        i += 1
    return board, queens

board,queens = CSP_backtracking(4)

print(board)

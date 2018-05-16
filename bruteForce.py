def initial(n,skip = (4,2)):
    "build a borard with n*(n+1)/2 holes "

    board = {}
    for c in range(0, 2*n, 2):
        d = 0
        for r in range((2*n - c )//2):
            board[(c+d, r)] = True
            d +=1
    if skip in board:
        board[skip]= False
    return board

def solve(board, path):
    """solve the board and updates path to reflect sequence of moves"""
    if len(path) == len(board) -2:
        return True
    for move in moves(board):
        path.append(move)
        makeMove(board,move)

        if solve(board, path):
            return True
        makeMove(board, move, undo=True)
        del path[-1]
    return False

#possible moves , each is (deltac, deltar)
directions = [(+4,0), (-4,0), (+2,+2), (-2,-2), (+2,-2), (-2,+2)]

#move is tripe [hole, deltac, deltar)
def moves(board):
    m = []
    for hole in board:
        if board[hole]:
            for deltac, deltar in directions:
                mid = (hole[0] + deltac//2, hole[1] + deltar//2)
                end = (hole[0] + deltac, hole[1] + deltar)
                if mid in board and board[mid] and \
                   end in board and not board[end]:
                    m.append([hole, deltac, deltar])
    return m

def makeMove(board, move, undo=False):
    hole , deltac, deltar = move
    mid = (hole[0] + deltac//2, hole[1] + deltar//2)
    end = (hole[0] + deltac, hole[1] + deltar)
    if not undo:
        board[hole] = False
        board[mid]= False
        board[end] = True
    else:
        board[hole] = True
        board[mid]= True
        board[end] = False


def solveSrecific(board):
    path = []
    solve(board, path)
    for move in path:
        print(move)



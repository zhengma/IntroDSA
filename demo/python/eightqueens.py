def isvalid(board: list) -> bool:
    current = board[:-1]
    attempt = board[-1]
    row = len(current)
    if attempt in current:
        return False
    for i in range(row):
        if row - i == attempt - current[i] or row - i ==  current[i] - attempt:
            return False
    return True

def print_board(board: list):
    for i in range(len(board)):
        print(chr(ord('A') + i) + str(board[i] + 1), end='\t')
    print("")

def eight_queen():
    board = [0]
    counter = 0
    while board:
        if isvalid(board):
            if len(board) < 8:
                board.append(0)
                continue
            else:
                print_board(board)
                counter += 1
        while board and board[-1] >= 7:
            board.pop()
        if board:
            board[-1] += 1
    print(counter)

if __name__ == "__main__":
    eight_queen()
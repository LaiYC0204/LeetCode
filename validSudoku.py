def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    for col in range(0, 9):
        for row in range(0, 9):
            if board[col][row] != '.':
                # 橫排確認
                for c_row in range(row + 1, 9):
                    if board[col][row] == board[col][c_row]:
                        print(f'橫排flase col:{col} row:{row} board[col][row]:{board[col][row]} board[col][c_row]:{board[col][c_row]}')
                        return False
                # 直排確認
                for c_col in range(col + 1, 9):
                    if board[col][row] == board[c_col][row]:
                        print(f'直排flase col:{col} row:{row} board[col][row]:{board[col][row]} board[c_col][row]:{board[c_col][row]}')
                        return False
                # 3*3區域確認
                chunk_col = (col // 3 * 3) + (col % 3)
                chunk_row = (row // 3 * 3) + (row % 3) + 1
                while chunk_col <= ((col // 3) * 3) + 2:
                    while chunk_row <= ((row // 3) * 3) + 2:
                        if board[col][row] == board[chunk_col][chunk_row]:
                            print(f'chuckFlase col:{col} row:{row} board[col][row]:{board[col][row]} board[chunk_col][chunk_row]:{board[chunk_col][chunk_row]}')
                            return False
                        chunk_row += 1
                    chunk_row = chunk_row = row // 3 * 3
                    chunk_col += 1
    return True

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board))
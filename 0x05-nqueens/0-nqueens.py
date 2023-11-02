#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in the given position on the board.

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N queens problem and print all solutions.

    Args:
        n (int): The size of the chessboard.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def print_board(board):
        positions = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    positions.append([row, col])
        print(positions)

    def solve(board, row):
        if row == n:
            print_board(board)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)

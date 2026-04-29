#!/usr/bin/python3
"""Module that solves the N queens problem using backtracking."""
import sys


def is_safe(board, row, col):
    """Check if placing a queen at board[row][col] is safe.

    Args:
        board (list): Current board state.
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in board:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively solve the N queens problem using backtracking.

    Args:
        n (int): Size of the board.
        row (int): Current row being processed.
        board (list): Current board state.
        solutions (list): List to store all solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve(n, row + 1, board, solutions)
            board.pop()


def nqueens(n):
    """Find and print all solutions to the N queens problem.

    Args:
        n (int): Size of the board.
    """
    solutions = []
    solve(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)

#!/usr/bin/python3
import sys


def is_safe(board, r, c):
    for i in range(r):
        if board[i] == c or board[i] - i == c - r or board[i] + i == c + r:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1


def print_solutions(solutions):
    for solution in solutions:
        print("[", end="")
        for i in range(len(solution)):
            print("[{}, {}]".format(i, solution[i]), end="")
            if i < len(solution) - 1:
                print(", ", end="")
        print("]")


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

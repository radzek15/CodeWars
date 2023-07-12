"""
Your task is to create a magic square for any positive odd integer N. The magic square contains the integers from 1 to N * N, arranged in an NxN matrix, such that the columns, rows and both main diagonals add up to the same number.

Note: use have to use the Siamese method for this task.
Examples:

n = 3
result = [
  [8, 1, 6],
  [3, 5, 7],
  [4, 9, 2]
]


n = 5
result = [
  [17, 24,  1,  8, 15],
  [23,  5,  7, 14, 16],
  [ 4,  6, 13, 20, 22],
  [10, 12, 19, 21,  3],
  [11, 18, 25,  2,  9]
]
"""


def magic_square(n):
    if n % 2:
        square = [[0]*n for e in range(n)]
        for i in range(n**2):
            x, y = (2 * (i//n) -i) % n, (n//2 + i - i//n)% n
            square[x][y] = i+1
        return square
    
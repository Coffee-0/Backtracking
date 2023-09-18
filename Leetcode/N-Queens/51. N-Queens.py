def solveNQueens(n):
    columns = set()
    positiveDiagonal = set()
    negativeDiagonal = set()
    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(row):
        if row == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        for col in range(n):
            if (
                col in columns
                or (row - col) in negativeDiagonal
                or (row + col) in positiveDiagonal
            ):
                continue

            columns.add(col)
            negativeDiagonal.add((row - col))
            positiveDiagonal.add((row + col))
            board[row][col] = "Q"

            backtrack(row + 1)

            columns.remove(col)
            negativeDiagonal.remove((row - col))
            positiveDiagonal.remove((row + col))
            board[row][col] = "."

    backtrack(0)
    return result


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         columns = set()
#         positiveDiagonal = set() # [ROW + COLUMN]
#         negativeDiagonal = set() # [ROW - COLUMN]
#         board = [["."] * n for i in range(n)]
#         result = []

#         def backtrack(row):
#             if row == n:
#                 solution = ["".join(row) for row in board]
#                 result.append(solution)
#                 return
#             for column in range(n):
#                 if ((column in columns) or
#                     (row + column) in positiveDiagonal or
#                     (row - column) in negativeDiagonal):
#                     continue
#                 columns.add(column)
#                 positiveDiagonal.add((row + column))
#                 negativeDiagonal.add((row - column))
#                 board[row][column] = 'Q'

#                 backtrack(row + 1)

#                 columns.remove(column)
#                 positiveDiagonal.remove((row + column))
#                 negativeDiagonal.remove((row - column))
#                 board[row][column] = "."

#         backtrack(0)
#         return result

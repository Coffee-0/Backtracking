def solveNQueens(n):
    columns = set()
    negativeDiagonal = set()
    positiveDiagonal = set()
    result = 0

    def backtrack(row):
        nonlocal result
        if row == n:
            result += 1
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

            backtrack(row + 1)

            columns.remove(col)
            negativeDiagonal.remove((row - col))
            positiveDiagonal.remove((row + col))

    backtrack(0)
    return result

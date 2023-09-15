class Solution:
    def exist(board, word):
        rows, columns = len(board), len(board[0])
        path = set()  # we do not want to revisit the same position

        def dfs(row, col, index):
            # Base Case: we found all characters in the word
            if len(word) == index:
                return True
            # Boundary Conditions
            if (
                (row < 0 or col < 0)
                or (row >= rows or col >= columns)
                or
                # Character Mismatch
                (board[row][col] != word[index])
                or
                # already we've visited the position
                ((row, col) in path)
            ):
                return False

            path.add((row, col))  # add current position to path
            # Recurse in all 4 adjacent positions
            result = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )
            path.remove((row, col))
            return result

        for row in range(rows):
            for col in range(columns):
                if dfs(row, col, 0):
                    return True
        return False

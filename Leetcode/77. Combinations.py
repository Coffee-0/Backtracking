def combine(n, k):
    def backtrack(start, path):
        # Base case: If the combination size equals k, add it to the result.
        if len(path) == k:
            result.append(path[:])  # Append a copy of the current combination
            return
        # Explore choices: Iterate through numbers, starting from 'start'.
        for i in range(start, n + 1):
            # Make a choice: Include the current number in the combination.
            path.append(i)
            # Recurse with the next number and the same combination size.
            backtrack(i + 1, path)
            # Undo the choice: Remove the last number to backtrack.
            path.pop()

    result = []
    backtrack(1, [])  # Start with 'start' = 1 and an empty combination.
    return result

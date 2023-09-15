def combinationSum3(k, n):
    def backtrack(start, path, current_sum):
        # Base case: If we've found a combination of k numbers that sum up to n, add it to the result.
        if len(path) == k and current_sum == n:
            result.append(path[:])  # Append a copy of the current combination
            return
        # If the current sum exceeds n or the number of elements in the path exceeds k, stop exploring.
        if current_sum > n or len(path) > k:
            return
        # Explore choices: Iterate through numbers from 'start' to 9.
        for i in range(start, 10):
            # Make a choice: Include the current number in the combination.
            path.append(i)
            # Recurse with the next number and updated sum.
            backtrack(i + 1, path, current_sum + i)
            # Undo the choice: Remove the last number to backtrack.
            path.pop()

    result = []
    backtrack(1, [], 0)
    return result

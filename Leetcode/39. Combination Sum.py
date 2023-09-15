def combination_sum(candidates, target):
    def backtrack(start, target, path):
        # Base case: If the target becomes zero, we found a valid combination.
        if target == 0:
            result.append(path[:])  # Append a copy of the current combination
            return
        # Explore choices: Iterate through candidates, starting from the 'start' index.
        for i in range(start, len(candidates)):
            # Check if the current candidate can be part of the solution.
            if candidates[i] <= target:
                # Make a choice: Include the current candidate in the combination.
                path.append(candidates[i])
                # Recurse with the same candidate (allowing duplicates) and updated target.
                backtrack(i, target - candidates[i], path)
                # Undo the choice: Remove the last candidate to backtrack.
                path.pop()

    result = []
    backtrack(0, target, [])
    return result

def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        # Base case: If the target becomes zero, we found a valid combination.
        if target == 0:
            result.append(path[:])  # Append a copy of the current combination
            return
        # Explore choices: Iterate through candidates, starting from 'start' index.
        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations.
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # Check if the current candidate can be part of the solution.
            if candidates[i] <= target:
                # Make a choice: Include the current candidate in the combination.
                path.append(candidates[i])
                # Recurse with the next number and updated target.
                backtrack(i + 1, target - candidates[i], path)
                # Undo the choice: Remove the last candidate to backtrack.
                path.pop()

    # Sort the input list to handle duplicates.
    candidates.sort()

    result = []
    backtrack(0, target, [])
    return result

def subsets(nums):
    def backtrack(start, path, result):
        # BaseCase: add the subset to result
        result.append(path[:])
        # Explore the entire range starting drom start
        for i in range(start, len(nums)):
            # Make a choice: Include the current element in the subset
            path.append(nums[i])
            # Recurse with the next element and 'start' index
            backtrack(i + 1, path, result)
            # Undo the choice: Exclude the current element
            path.pop()

    result = []
    backtrack(0, [], result)
    return result

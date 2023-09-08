def subsets(nums):
    def backtrack(nums, start, path, result):
        # Basecase: add current subset to path
        result.append(path[:])
        # Explore Choices: Iterate from start to end
        for i in range(start, len(nums)):
            # make choice: Include current element in the subset
            path.append(nums[i])
            # recurse with next element as start
            backtrack(nums, i + 1, path, result)
            # undo choice: exclude the current element
            path.pop()

    result = []
    backtrack(nums, 0, [], result)
    return result


nums = [1, 2, 3]
print(subsets(nums))

def subsetsWithDuplicates(nums):
    def backtrack(start, path):
        # Basecase: Add current subset to path
        result.append(path[:])
        # Explore choices: Iterate from start to end
        for i in range(start, len(nums)):
            # avoid duplicates by checking if the previous element was the same as current
            if i > start and nums[i] == nums[i - 1]:
                continue
            # make choice: Include current element
            path.append(nums[i])
            # Recurse with the next element as 'start' index
            backtrack(i + 1, path)
            # make choice: Exclude the current number
            path.pop()

    # Sort the input list to handle duplicates
    nums.sort()
    result = []
    backtrack(0, [])
    return result


nums = [1, 2, 2]
print(subsetsWithDuplicates(nums))

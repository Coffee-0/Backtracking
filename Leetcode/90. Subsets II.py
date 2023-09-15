def subsetsWithDup(nums):
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        # Explore choices: Iterate through elements from 'start' to the end
        for i in range(start, len(nums)):
            # Avoid duplicates by skipping elements that are the same as the previous element
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Make a choice: Include the current element in the subset
            path.append(nums[i])
            # Recurse with the next element and 'start' index
            backtrack(i + 1, path)
            # Undo the choice: Remove the last element to backtrack
            path.pop()

    # Sort the input list to handle duplicates
    nums.sort()
    result = []
    backtrack(0, [])
    return result

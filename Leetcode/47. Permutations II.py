def permuteUnique(nums):
    def backtrack(frequency, path, result):
        # BaseCase: we found a valid permutation
        if len(nums) == len(path):
            result.append(path[:])
            return
        # Explore Choices: Iterate over the frequencyMap instead of nums
        for n in frequency:
            # if the frequency of element n in map is more than 0 then it can be used as an element in the permutation.
            if frequency[n] > 0:
                # Make Choice: decrement the frequency of n by 1 and add it to path
                frequency[n] -= 1
                path.append(n)
                # Backtrack: Recurse with updated path and updated values in frequency Mapping
                backtrack(frequency, path, result)
                # Undo the Choice: increment the frequency of n by 1 and pop it to path, undoind what we did before
                frequency[n] += 1
                path.pop()

    # frequency dictionary we eliminate the chances of iterating over duplicates
    frequencyMap = {}
    for n in nums:
        frequencyMap[n] = frequencyMap.get(n, 0) + 1

    result = []
    backtrack(frequencyMap, [], result)
    return result

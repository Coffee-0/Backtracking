def permutations(nums):
    def backtrack(nums, path, result):
        # BaseCase: We have a valid permutation
        # len(nums) == len(path) : means we have all the values from nums in path which forms a permutation
        if len(nums) == len(path):
            result.append(path[:])
            return
        # Explore choices: Iterate through nums
        for number in nums:
            # skip the number if it is already in the path, (we dont want duplicates)
            if number in path:
                continue
            # make a choice
            path.append(number)
            backtrack(nums, path, result)  # Recurse
            # undo the choice
            path.pop()

    result = []
    backtrack(nums, [], result=result)
    return result


nums = [1, 2, 3]
print(permutations(nums))

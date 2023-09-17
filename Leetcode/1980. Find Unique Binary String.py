def findDifferentBinaryString(nums):
    binarySet = set(nums)

    def backtrack(path):
        if len(path) == len(nums):
            return None if path in binarySet else path
        for digit in ["0", "1"]:
            path += digit
            result = backtrack(path)
            if result:
                return result
            path = path[:-1]

    return backtrack("")

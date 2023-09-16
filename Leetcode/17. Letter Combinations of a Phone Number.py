def letterCombinations(digits):
    if not digits:
        return []
    digitToLetters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(index, path):
        if index == len(digits):
            result.append(path[:])
            return
        letters = digitToLetters[digits[index]]
        for letter in letters:
            path += letter
            backtrack(index + 1, path)
            path = path[:-1]

    result = []
    backtrack(0, "")
    return result

def partition(s):
    # helper function to find out if a given substring is a palindrome or not
    def isPalindrome(substring, left, right):
        while left < right:
            if substring[left] != substring[right]:
                return False
            left, right = left + 1, right - 1
        return True

    def backtrack(start, path):
        # Base case: If we've reached the end of the string, add the current partition to the result
        if start == len(s):
            result.append(path[:])
            return
        # Iterate through the string from 'start' to 'end'
        for end in range(start, len(s)):
            # Check if current string is palindrome
            if isPalindrome(s, start, end):
                # Make a choice: Add the current substring to the partition path
                path.append(s[start : end + 1])
                # Recurse with the updated 'start' and 'path'
                backtrack(end + 1, path)
                # Undo the choice (backtrack): Remove the last element from the path
                path.pop()

    result = []
    backtrack(0, [])
    return result

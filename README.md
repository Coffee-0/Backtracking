# My Brain No Understand Backtracking

## Notes: do I need these ?

- **Backtracking** is a technique used to solve problems involving choices and constraints, such as finding all possible solutions, permutations, combinations, or paths in a problem space. It explores all possible states/solutions to a problem by incrementally building a solution and undoing it if found to be invalid.

## More Notes that no one needs

- **Brute Force** approach explores all possible solutions and may select the desired solution, but it can be inefficient for problems with a large solution space.
- **Backtracking** approach also explores all possible solutions, especially when there are multiple valid solutions, and it backtracks when it encounters invalid solutions.
- **Dynamic Programming** uses a more structured approach to find optimal solutions by breaking down problems into smaller subproblems and reusing intermediate results, which can be more efficient than a pure brute force approach.

## Steps to writing a backtracking solution

1. **Define the Backtrack Function**: Create a recursive function that will explore different possibilities and maintain a partial solution.
2. **Base Case**: Define a base case that determines when to stop the recursion. This usually involves checking if you've reached a valid or invalid solution.
3. **Backtracking Logic**: Implement the backtracking logic within your function. This includes making choices, exploring them, and undoing them if necessary.
4. **Explore Choices**: Within your backtracking function, iterate through the possible choices you can make at the current step.
5. **Recursive Calls**: Make recursive calls with updated state, taking into account the choice made at the current step.
6. **Undo Choices**: After exploring a choice and its subproblems, undo any changes you made to the state to backtrack and try a different choice.

## Backtracking Permutations: Leetcode

Let's Solve some questions on permutations to understand backtracking better.

**[46. Permutations](https://leetcode.com/problems/permutations/)**
Given an array `nums` of distinct integers, return _all the possible permutations_.

```python
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
            # make a choice: Include the current number
            path.append(number)
            backtrack(nums, path, result)  # Recurse with new path
            # undo the choice: exclude the current number
            path.pop()

    result = []
    backtrack(nums, [], result=result)
    return result
```

**[47. Permutations II](https://leetcode.com/problems/permutations-ii/)**
Given a collection of numbers, `nums`, that might contain duplicates, return _all possible unique permutations **in any order**._

```python
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

```

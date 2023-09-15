# The Backtracking Guide

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

`- In this case we are just making a small change: Instead of Iterating over the input array, convert it to a frequency map and iterate over the frequency map.`

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

## Backtracking on Subsets: Leetcode

Now let's Solve some questions on subsets.

**[78. Subsets](https://leetcode.com/problems/subsets/)**
Given an integer array `nums` of **unique** elements, return \_all possible subsets.
The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

```python
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

```

**[90. Subsets II](https://leetcode.com/problems/subsets-ii/)**
Given an integer array `nums` that may contain duplicates, return _all possible_
_subsets_.

```python
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


```

## Backtracking on Combinations: Leetcode

Now let's Solve some questions on Combinations.

**[77. Combinations](https://leetcode.com/problems/combinations/)**
Given two integers `n` and `k`, return _all possible combinations of_ `k` _numbers chosen from the range_ `[1, n]`.

```python
def combine(n, k):
    def backtrack(start, path):
        # Base case: If the combination size equals k, add it to the result.
        if len(path) == k:
            result.append(path[:])  # Append a copy of the current combination
            return
        # Explore choices: Iterate through numbers, starting from 'start'.
        for i in range(start, n + 1):
            # Make a choice: Include the current number in the combination.
            path.append(i)
            # Recurse with the next number and the same combination size.
            backtrack(i + 1, path)
            # Undo the choice: Remove the last number to backtrack.
            path.pop()

    result = []
    backtrack(1, [])  # Start with 'start' = 1 and an empty combination.
    return result


```

**[39. Combination Sum](https://leetcode.com/problems/combination-sum/)**
Given an array of **distinct** integers `candidates` and a target integer `target`, return _a list of all **unique combinations** of_ `candidates` _where the chosen numbers sum to_ `target`_._
The **same** number may be chosen from `candidates` an **unlimited number of times**.

```python
def combination_sum(candidates, target):
    def backtrack(start, target, path):
        # Base case: If the target becomes zero, we found a valid combination.
        if target == 0:
            result.append(path[:])  # Append a copy of the current combination
            return
        # Explore choices: Iterate through candidates, starting from the 'start' index.
        for i in range(start, len(candidates)):
            # Check if the current candidate can be part of the solution.
            if candidates[i] <= target:
                # Make a choice: Include the current candidate in the combination.
                path.append(candidates[i])
                # Recurse with the same candidate (allowing duplicates) and updated target.
                backtrack(i, target - candidates[i], path)
                # Undo the choice: Remove the last candidate to backtrack.
                path.pop()

    result = []
    backtrack(0, target, [])
    return result

```

**[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)**
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.
Each number in `candidates` may only be used **once** in the combination.

```python
def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        # Base case: If the target becomes zero, we found a valid combination.
        if target == 0:
            result.append(path[:])  # Append a copy of the current combination
            return
        # Explore choices: Iterate through candidates, starting from 'start' index.
        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations.
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # Check if the current candidate can be part of the solution.
            if candidates[i] <= target:
                # Make a choice: Include the current candidate in the combination.
                path.append(candidates[i])
                # Recurse with the next number and updated target.
                backtrack(i + 1, target - candidates[i], path)
                # Undo the choice: Remove the last candidate to backtrack.
                path.pop()

    # Sort the input list to handle duplicates.
    candidates.sort()

    result = []
    backtrack(0, target, [])
    return result

```

**[216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)**
Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

- Only numbers `1` through `9` are used.
- Each number is used **at most once**.

Return _a list of all possible valid combinations_.

```python
def combinationSum3(k, n):
    def backtrack(start, path, current_sum):
        # Base case: If we've found a combination of k numbers that sum up to n, add it to the result.
        if len(path) == k and current_sum == n:
            result.append(path[:])  # Append a copy of the current combination
            return
        # If the current sum exceeds n or the number of elements in the path exceeds k, stop exploring.
        if current_sum > n or len(path) > k:
            return
        # Explore choices: Iterate through numbers from 'start' to 9.
        for i in range(start, 10):
            # Make a choice: Include the current number in the combination.
            path.append(i)
            # Recurse with the next number and updated sum.
            backtrack(i + 1, path, current_sum + i)
            # Undo the choice: Remove the last number to backtrack.
            path.pop()

    result = []
    backtrack(1, [], 0)
    return result


```

- **If you need more problems on backtracking you can check the leetcode folder.**

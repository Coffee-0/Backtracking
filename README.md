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
https://github.com/Coffee-0/Backtracking/blob/c0288c39aa05400e326b3a0fd24c9032792c22be/Leetcode/46.%20Permutations.py

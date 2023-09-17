class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, stack = [], []

        def backtrack(open, close):
            # valid == open == close == n
            if open == close == n:
                result.append("".join(stack))
                return
            # only add open paranthesis if open < n
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            # only add a closing paranthesis if open > close
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return result

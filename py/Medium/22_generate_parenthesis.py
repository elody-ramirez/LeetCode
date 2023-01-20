# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8

class Solution(object):
    """Solution"""
    def generate_parenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IF open == closed == n

        stack = []
        res = []

        def back_track(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                back_track(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                back_track(openN, closedN + 1)
                stack.pop()

        back_track(0,0)
        return res

print(Solution().generate_parenthesis(3))
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

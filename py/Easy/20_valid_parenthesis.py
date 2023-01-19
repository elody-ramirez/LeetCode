# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# FIRST SOLUTION--------
# class Solution(object):
#     def is_valid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         pairs = {')': '(', '}': '{', ']': '['}
#         stack = []
#         for c in s:
#             if c in pairs:
#                 if stack and stack[-1] == pairs[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         return True if not stack else False

class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != pairs[c]:
                return False
        if len(stack) == 0:
            return True

string = '{([])})'
print(Solution().is_valid(string))        # True

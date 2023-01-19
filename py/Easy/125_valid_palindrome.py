# A phrase is a palindrome if , after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# O(N) Time and O(1) Space solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, c):
        """
        :type c: str
        :rtype: bool
        """
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
                
# O(N) Space and Time solution because i use a new string
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         newStr = ""

#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded
# back to the original list of strings.

# Please implement encode and decode

# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

# O(N) Time 0(1) Space Complexity for encode and decode. N is the
# total number of characters in the list of words
class Solution:
    """
    Solution
    """

    def encode(self, strs):
        # write your code here
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, string):
        # write your code here
        """
        @param: string: A string
        @return: dcodes a single string to a list of strings
        """
        res, i = [], 0
        
        while i < len(string):
            j = i 
            while string[j] != '#':
                j += 1
            length = int(string[i:j])
            res.append(string[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

input1 = ["lint", "code", "love", "you"]
input2 = ["we", "say", ":", "yes"]

encoded1 = Solution().encode(input1)
encoded2 = Solution().encode(input2)
print(encoded1)
print(encoded2)

print(Solution().decode(encoded1))
print(Solution().decode(encoded2))

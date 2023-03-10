# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all
# the original letters exactly once.


# Example 1:

# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
from collections import defaultdict

# O(m * n) Time 0(n) Space Complexity
# m is the number of strings given and n is the avg length of
# strings since we go through each character
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()

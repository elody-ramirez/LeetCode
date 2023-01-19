# Given an unsorted array of integers nums, return the length of
# the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# O(n) Time 0(n) Space Complexity
class Solution(object):
    """Solution"""
    def longest_consecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in num_set:
                length = 0
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest

input1 = [100, 4, 200, 1, 3, 2]
print(Solution().longest_consecutive(input1))

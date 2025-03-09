class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        We'll use here "Greedy algorithms"
        """
        max_index = 0
        for k in range(len(nums)):
            if k > max_index:
                return False
            max_index = max(max_index, nums[k] + k)
            if max_index >= len(nums) - 1:
                return True

        return False


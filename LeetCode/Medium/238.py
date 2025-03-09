class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length

        left = 1
        for k in range(length):
            result[k] *= left
            left *= nums[k]
        right = 1
        for k in range(length - 1, -1, -1):
            result[k] *= right
            right *= nums[k]

        return result



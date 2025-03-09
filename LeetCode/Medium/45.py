class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_jumps = 0
        cur_end = 0 # Текущая граница прыжка
        max_reach = 0
        for k in range(len(nums) - 1):
            max_reach = max(max_reach, nums[k] + k)
            if k == cur_end:
                cur_end = max_reach
                count_jumps += 1
        return count_jumps

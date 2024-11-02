class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for index, num in enumerate(nums):
            complement = target - num # 9 - 4 = 5

            if complement in num_map:
                return [num_map[complement], index]


            num_map[num] = index

        return []


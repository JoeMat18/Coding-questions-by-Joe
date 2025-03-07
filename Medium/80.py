class Solution(object):
    def removeDuplicates(self, nums):
        slow = 2
        for k in range(2, len(nums)):
            if nums[k] != nums[slow - 2]:
                nums[slow] = nums[k]
                slow += 1
        return slow



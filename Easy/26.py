class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for k in range(1, len(nums)):
            if nums[slow] != nums[k]:
                slow += 1
                nums[slow] = nums[k]
        return slow + 1
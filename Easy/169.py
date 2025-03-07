class Solution(object):
    def majorityElement(self, nums):
        majorElem = 0
        count = 0
        for num in nums:
            if count == 0:
                majorElem = nums[num]
            count += 1 if majorElem == nums[num] else -1

        return majorElem
class Solution(object):
    def removeElement(self, nums, val):
        slow = 0 # указатель для чистых элементов
        for k in range(len(nums)):
            if nums[k] != val:
                nums[slow] = nums[k]
                slow += 1
        return slow

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1 # The last element of nums1 (not zero)
        p2 = n - 1 # The lest element of nums2
        p = m + n - 1 # Последний элемент nums1, куда будем вставлять
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:  # Берём большее число
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        """
        Если остались элементы в nums2, то копируем их в nums1
        nums1 = [0, 0, 0], m = 0
        nums2 = [1, 2, 3], n = 3
        """
        nums1[:p2 + 1] = nums2[:p2 + 1]


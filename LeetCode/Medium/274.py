class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_count = 0
        citations.sort(reverse = True)
        for k, citation in enumerate(citations):
            if citation >= k + 1:
                h_count += 1
            else:
                break
        return h_count
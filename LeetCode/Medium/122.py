class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for k in range(1, len(prices)):
            if prices[k] > prices[k - 1]:
                maxProfit += prices[k] - prices[k - 1]
        return maxProfit

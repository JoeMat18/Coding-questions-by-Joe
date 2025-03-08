class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)

        return max_profit
    def maxProfitSecond(self, prices):
        left = 0
        right = 1
        max_profit = 0

        while right > len(prices):
            if (prices[right] > prices[left]):
                max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
            left += 1
        return max_profit



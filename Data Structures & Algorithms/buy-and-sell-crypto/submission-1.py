class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0, 1
        maxProfit = 0
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
            elif prices[i] > prices[j]:
                i = j
        return maxProfit

                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for x in range(len(prices) -1 ):
            for y in range(x + 1,len(prices) ):
                diff = prices[y] - prices[x]
                if(diff > max):
                    max = diff

        return max
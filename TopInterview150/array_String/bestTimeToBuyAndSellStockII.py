class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        totalPrice = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                totalPrice += prices[i - 1] - minPrice
                minPrice = prices[i]
            else:
                if i == len(prices) - 1:
                    totalPrice += prices[i] - minPrice

        return totalPrice
    
    def GPTmaxProfit(self, prices):
        totalProfit = 0

        # 只要價格上升我就做交易
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                totalProfit += prices[i] - prices[i - 1]

        return totalProfit

    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
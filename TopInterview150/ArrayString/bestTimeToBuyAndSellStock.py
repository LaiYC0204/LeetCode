class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxPrice = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif maxPrice < price - minPrice:
                maxPrice = price - minPrice

        return maxPrice

    
s = Solution()
print(s.maxProfit([2,1,4]))
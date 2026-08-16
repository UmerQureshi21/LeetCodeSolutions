class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        max_profit = 0
        bp = 0
        sp = 1
        while bp < len(prices):
            if sp<len(prices):
                if prices[sp] > prices[bp]:
                    if prices[sp]-prices[bp] > max_profit:
                        max_profit = prices[sp]-prices[bp]
                sp += 1
            else:
                bp +=1
                sp = bp +1
        return max_profit


            

print(Solution().maxProfit([1]))
        


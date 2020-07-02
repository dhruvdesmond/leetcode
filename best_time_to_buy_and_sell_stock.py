class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        prev = prices[0]
        curr_profit=0
        m = 0

        for i in range(1,len(prices)):
            if prices[i] < prev:
                
                prev = prices[i]
                curr_profit=0
            else:
                curr_profit = prices[i]-prev
            m = max(m,curr_profit)
        m = max(curr_profit,m)
        return m
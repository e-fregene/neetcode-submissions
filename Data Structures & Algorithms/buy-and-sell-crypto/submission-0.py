class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices[i] is price on ith day
        """

        # keep track of small and largest. Calc as you go
        # want sell(r) >. [1,2,3,5]. Buy low sell high, sell future

        l,r=0,1

        money=0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            money= max(money, sell-buy)
            if prices[r] >= prices[l]:
                sell = prices[r]
            else:
                l=r
                buy = prices[l]
            r+=1
                
                


        return money
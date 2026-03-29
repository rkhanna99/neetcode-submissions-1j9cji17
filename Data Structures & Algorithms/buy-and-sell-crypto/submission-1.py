class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize values for the max profit and the current lowest price
        max_profit = 0
        lowest_price = 101

        while len(prices) > 1:
            curr = prices.pop(0)
            if curr >= prices[0]:
                continue
            else:
                if curr < lowest_price:
                    lowest_price = curr 
                curr_profit = prices[0] - lowest_price
                if max_profit < curr_profit:
                    max_profit = curr_profit

        return max_profit
        

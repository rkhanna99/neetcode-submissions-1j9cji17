class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sell_value = -1

        for price in reversed(prices):
            if price > sell_value:
                sell_value = price
            else:
                curr_profit = sell_value - price
                if curr_profit > max_profit:
                    max_profit = curr_profit
            prices.pop()

        return max_profit
            
        
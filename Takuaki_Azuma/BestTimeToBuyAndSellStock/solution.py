from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from buying and selling a stock.
        
        Args:
            prices: A list of integers representing the stock price on each day.
        
        Returns:
            The maximum profit achievable. Returns 0 if no profit is possible.
        """
        # Initialize min_price to a very large number (infinity)
        # min_price を非常に大きな数（無限大）で初期化します
        min_price = float('inf')
        
        # Initialize max_profit to 0
        # max_profit を 0 で初期化します
        max_profit = 0
        
        for price in prices:
            # 1. Update the minimum price so far
            # 1. これまでの最安値を更新します
            if price < min_price:
                min_price = price
            
            # 2. Calculate profit if we sell today
            # 2. 今日売った場合の利益を計算します
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

if __name__ == "__main__":
    # Test cases
    solution = Solution()
    
    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices1}, Max Profit: {solution.maxProfit(prices1)}") # Expected: 5
    
    # Example 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Prices: {prices2}, Max Profit: {solution.maxProfit(prices2)}") # Expected: 0

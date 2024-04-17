"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Examples:
Input: [100, 80, 60, 70, 60, 75, 85]
Output: [1, 1, 1, 2, 1, 4, 6]

Problem source: LeetCode

Usage: online_stock_span.py <comma_separated_nums>
"""

from utils import read_int_array
import sys

class StockSpanner:
    def __init__(self):
        self.values = []

    def next(self, price: int) -> int:
        span = 1

        while self.values and self.values[-1][0] <= price:
            _last_price, last_span = self.values.pop()
            span += last_span

        self.values.append((price, span))

        return span
    

if __name__ == "__main__":
  args = read_int_array(sys.argv[1])
  
  stock_spanner = StockSpanner()
  for arg in args:
    print(stock_spanner.next(arg), end=" ")
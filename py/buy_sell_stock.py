"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0

Problem source: LeetCode

Usage: buy_sell_stock.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def max_profit(prices: List[int]) -> int:
  min_value = prices[0]
  best_profit = 0

  for i in range(1, len(prices)):
    if prices[i] < prices[i-1]:
      min_value = min(min_value, prices[i])
    else:
      best_profit = max(best_profit, prices[i] - min_value)

  return best_profit


if __name__ == "__main__":
  print(max_profit(read_int_array(sys.argv[1])))
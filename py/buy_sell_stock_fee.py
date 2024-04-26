"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

Examples:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Problem source: LeetCode

Usage: buy_sell_stock_fee.py <comma_separated_nums> <fee>
"""

from typing import List
from utils import read_int_array
import sys

def max_profit(prices: List[int], fee: int) -> int:
  current_profit = -1
  total_profit = 0
  current_min = prices[0]
  current_max = -1

  for price in prices[1:]:
    if price < current_min or price + fee < current_max:
      if current_profit > 0:
        total_profit += current_profit

      current_min = price
      current_max = -1
      current_profit = -1
      continue

    margin = price - current_min - fee
    if margin > current_profit:
      current_profit = margin
      current_max = price

  if current_profit > 0:
    total_profit += current_profit


  return total_profit


if __name__ == "__main__":
  print(max_profit(read_int_array(sys.argv[1]), int(sys.argv[2])))
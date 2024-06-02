"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples:
Input: coins = [1,2,5], amount = 11
Output: 3

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Problem source: LeetCode

Usage: coin_change.py <comma_separated_nums> <amount>
"""

from typing import List
from utils import read_int_array
import sys

def coin_change(coins: List[int], amount: int) -> int:
  out_of_bounds = amount+1
  dp = [out_of_bounds] * (amount+1)
  dp[0] = 0

  for coin in coins:
    for i in range(coin, amount + 1):
      dp[i] = min(dp[i], dp[i-coin]+1)

  return dp[amount] if dp[amount] != out_of_bounds else -1


if __name__ == "__main__":
  print(coin_change(read_int_array(sys.argv[1]), int(sys.argv[2])))
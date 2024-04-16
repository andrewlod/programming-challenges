"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Examples:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

Problem source: LeetCode

Usage: kids_with_candies.py <comma_separated_nums> <extraCandies>
"""

from typing import List
from utils import read_int_array
import sys

def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
  max_candies = max(candies)

  result = [child_candies + extraCandies >= max_candies for child_candies in candies]

  return result


if __name__ == "__main__":
  print(kids_with_candies(read_int_array(sys.argv[1]), int(sys.argv[2])))
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Examples:
Input: cost = [10,15,20]
Output: 15

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

Problem source: LeetCode

Usage: min_cost_climbing_stairs.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def min_cost_climbing_stairs(cost: List[int]) -> int:
    last = cost[-1]
    second_to_last = cost[-2]

    for i in range(len(cost)-3, -1, -1):
        current_cost = cost[i] + min(last, second_to_last)
        last = second_to_last
        second_to_last = current_cost

    return min(last, second_to_last)


if __name__ == "__main__":
    print(min_cost_climbing_stairs(read_int_array(sys.argv[1])))
"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Examples:
Input: nums = [1,2,3,1]
Output: 2

Input: nums = [1,2,1,3,5,6,4]
Output: 5

Problem source: LeetCode

Usage: find_peak_element.py
"""

from typing import List
from utils import read_int_array
import sys

def find_peak_element(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        midpoint = (left + right) // 2

        left_val = nums[midpoint-1] if midpoint > 0 else float('-inf')
        right_val = nums[midpoint+1] if midpoint < len(nums)-1 else float('-inf')
        current_val = nums[midpoint]

        if current_val > left_val and current_val > right_val:
            return midpoint
        
        if left_val < right_val:
            left = midpoint + 1
        else:
            right = midpoint

    return left


if __name__ == "__main__":
    print(find_peak_element(read_int_array(sys.argv[1])))
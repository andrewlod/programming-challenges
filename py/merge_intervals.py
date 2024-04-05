"""
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Examples:
Input: 1,3 2,6 8,10 15,18
Output: [[1,6],[8,10],[15,18]]

Input: 1,4 4,5
Output: [[1,5]]

Problem source: LeetCode

Usage: merge_intervals.py <s> <t>
"""

from typing import List
import sys

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges intervals in a list of intervals.

    Parameters:
    intervals (List[List[int]]): List of intervals, where each interval is a pair of integers

    Returns:
    bool: Merged intervals
    """
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        current = merged[-1]

        if current[1] >= interval[0]:
            current[1] = max(current[1], interval[1])
        else:
            merged.append(interval)

    return merged

if __name__ == "__main__":
    print(merge(
        [
            list(map(int, interval.split(','))) for interval in sys.argv[1:]
        ]
    ))
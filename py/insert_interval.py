"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Examples:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

Problem source: LeetCode

Usage: insert_interval.py "<comma_separated_interval1> <comma_separated_interval2> ..." <comma_separated_new_interval>
"""

from typing import List
from utils import read_int_matrix, read_int_array
import sys

def is_overlapping(interval1: List[List[int]], interval2: List[List[int]]) -> bool:
  return interval2[0] <= interval1[0] <= interval2[1] or interval1[0] <= interval2[0] <= interval1[1]

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  if len(intervals) == 0:
    return [newInterval]
  
  new_list = []
  current_test = intervals[0]
  if is_overlapping(newInterval, current_test):
    current_test = [min(newInterval[0], current_test[0]), max(newInterval[1], current_test[1])]
  elif newInterval[1] < current_test[0]:
    new_list.append(newInterval)

  for i, interval in enumerate(intervals[1:]):
    if is_overlapping(interval, current_test):
      current_test[1] = interval[1]
    else:
      new_list.append(current_test)
      current_test = interval

    if is_overlapping(newInterval, current_test):
      current_test = [min(newInterval[0], current_test[0]), max(newInterval[1], current_test[1])]
    elif newInterval[1] < current_test[0] and intervals[i][1] < newInterval[0]:
      new_list.append(newInterval)

  new_list.append(current_test)

  if newInterval[0] > current_test[1]:
    new_list.append(newInterval)

  return new_list


if __name__ == "__main__":
  print(insert(read_int_matrix(sys.argv[1]), read_int_array(sys.argv[2])))
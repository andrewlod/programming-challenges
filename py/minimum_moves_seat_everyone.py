"""
There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.

Examples:
Input: seats = [3,1,5], students = [2,7,4]
Output: 4

Input: seats = [4,1,5,9], students = [1,3,2,6]
Output: 7

Input: seats = [2,2,6,6], students = [1,3,2,6]
Output: 4

Problem source: LeetCode

Usage: minimum_moves_seat_everyone.py <comma_separated_seats> <comma_separated_students>
"""

from typing import List
from functools import reduce
from utils import read_int_array
import sys

def min_moves_to_seat(seats: List[int], students: List[int]) -> int:
  sorted_seats = sorted(seats)
  sorted_students = sorted(students)
  return reduce(lambda acc, val: acc + abs(val[0] - val[1]), zip(sorted_seats, sorted_students), 0)


if __name__ == "__main__":
  print(min_moves_to_seat(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
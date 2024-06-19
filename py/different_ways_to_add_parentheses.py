"""
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Examples:
Input: expression = "2-1-1"
Output: [0,2]

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]

Problem source: LeetCode

Usage: different_ways_to_add_parentheses.py <expression>
"""

from typing import List
import sys

operations = {
  "+": lambda a, b: a + b,
  "-": lambda a, b: a - b,
  "*": lambda a, b: a * b
}

def diff_ways_to_compute(expression: str) -> List[int]:
  integers = []
  operators = []
  current_val = 0

  for char in expression:
    if char.isdigit():
      current_val *= 10
      current_val += int(char)
    else:
      integers.append(current_val)
      current_val = 0
      operators.append(char)

  integers.append(current_val)

  def backtrack(start: int, end: int) -> List[int]:
    nonlocal integers, operators
    if start == end:
      return [integers[start]]
    elif end - start == 1:
      return [operations[operators[start]](integers[start], integers[end])]

    possibilities = []
    for i in range(start, end):
      left = backtrack(start, i)
      right = backtrack(i+1, end)
      for left_perm in left:
        for right_perm in right:
          possibilities.append(operations[operators[i]](left_perm, right_perm))

    return possibilities

  return backtrack(0, len(integers)-1)


if __name__ == "__main__":
  print(diff_ways_to_compute(sys.argv[1]))
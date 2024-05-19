"""
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

"Push": pushes an integer to the top of the stack.
"Pop": removes the integer on the top of the stack.
You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
If the stack is not empty, pop the integer at the top of the stack.
If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

Examples:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]

Input: target = [1,2], n = 4
Output: ["Push","Push"]

Problem source: LeetCode

Usage: build_array_with_stack_operations.py <comma_separates_nums> <n>
"""

from typing import List
from utils import read_int_array
import sys

def build_array(target: List[int], n: int) -> List[str]:
  next_target = 0
  operations = []

  for i in range(1, n+1):
    if i == target[next_target]:
      operations.append("Push")
      next_target += 1
      
      if next_target >= len(target):
        break
    else:
      operations.append("Push")
      operations.append("Pop")
  
  return operations


if __name__ == "__main__":
  print(build_array(read_int_array(sys.argv[1]), int(sys.argv[2])))
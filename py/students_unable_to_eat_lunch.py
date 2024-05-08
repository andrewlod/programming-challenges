"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

Examples:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

Problem source: LeetCode

Usage: students_unable_to_eat_lunch.py <comma_separated_students> <comma_separated_sandwiches>
"""

from typing import List
from collections import deque
from utils import read_int_array
import sys

def count_students(students: List[int], sandwiches: List[int]) -> int:
  count_students = [0, 0]

  for student in students:
    count_students[student] += 1

  students_queue = deque(students)
  sandwich_ptr = 0

  while sandwich_ptr < len(sandwiches):
    current_student = students_queue.popleft()
    if sandwiches[sandwich_ptr] == current_student:
      count_students[current_student] -= 1
      sandwich_ptr += 1
      continue

    if count_students[1-current_student] == 0:
      return count_students[current_student]

    students_queue.append(current_student)
          

  return 0


if __name__ == "__main__":
  print(count_students(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
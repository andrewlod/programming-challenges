"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

Problem source: LeetCode

Usage: course_schedule.py <num_courses> <course1,dependency1 course2,dependency2 ...>
"""

from typing import List
from utils import read_int_matrix
import sys

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
  pre_reqs = {}

  for course, dependency in prerequisites:
    if course not in pre_reqs:
      pre_reqs[course] = set([dependency])
    else:
      pre_reqs[course].add(dependency)

  for course, dependencies in pre_reqs.items():
    visited = set()
    courses_to_find = dependencies
    while courses_to_find:
      new_courses = set()

      for dependency in courses_to_find:
        if dependency in visited:
          continue

        if dependency == course:
          return False

        visited.add(dependency)
        if dependency in pre_reqs:
          new_courses = new_courses | pre_reqs[dependency]

      courses_to_find = new_courses

  return True


if __name__ == "__main__":
  print(can_finish(int(sys.argv[1]), read_int_matrix(sys.argv[2])))
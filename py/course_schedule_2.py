"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Examples:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]

Input: numCourses = 1, prerequisites = []
Output: [0]

Problem source: LeetCode

Usage: course_schedule_2.py <num_courses> <course1,prereq1> <course2,prereq2> ...
"""

from typing import List, Set, Dict
from utils import read_int_matrix
import sys

def add_prereqs(stack: List[int], course: int, prereqs: Dict[int, List[int]], remaining_courses: Set[int], visited: Set[int]) -> bool:
    if course in visited:
        return False

    course_prereqs = prereqs[course]
    visited.add(course)
    for adj_course in course_prereqs:
        if adj_course not in remaining_courses:
            continue

        if adj_course in prereqs:
            add_prereqs(stack, adj_course, prereqs, remaining_courses, visited)

        if adj_course not in remaining_courses:
            return False
        
        stack.append(adj_course)
        remaining_courses.remove(adj_course)

    return True


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
  remaining_courses = set([i for i in range(numCourses)])

  prereqs = {}
  for course, prereq in prerequisites:
    if course not in prereqs:
      prereqs[course] = [prereq]
    else:
      prereqs[course].append(prereq)

  stack = []
  for course in range(numCourses):
    if course not in remaining_courses:
      continue
    
    if course in prereqs:
      visited = set()
      possible = add_prereqs(stack, course, prereqs, remaining_courses, visited)
      if not possible:
        return []

    if course not in remaining_courses:
      return []
    
    stack.append(course)
    remaining_courses.remove(course)
  
  for course in remaining_courses:
    stack.append(course)

  return stack


if __name__ == "__main__":
    print(find_order(int(sys.argv[1]), read_int_matrix("".join(sys.argv[2:]))))
"""
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

It must start with a single slash '/'.
Directories within the path should be separated by only one slash '/'.
It should not end with a slash '/', unless it's the root directory.
It should exclude any single or double periods used to denote current or parent directories.
Return the new path.

Examples:
Input: path = "/home/"
Output: "/home"

Input: path = "/home//foo/"
Output: "/home/foo"

Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"

Input: path = "/../"
Output: "/"

Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"

Problem source: LeetCode

Usage: simplify_path.py <path>
"""

import sys

def simplify_path(path: str) -> str:
  directories = path.split("/")
  stack = []

  for directory in directories:
    if len(directory) == 0 or directory == "." or (directory == ".." and not stack):
      continue

    if directory == "..":
      stack.pop()
    else:
      stack.append(directory)

  return "/" + "/".join(stack)


if __name__ == "__main__":
  print(simplify_path(sys.argv[1]))
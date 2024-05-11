"""
You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

Return the array answer as described above.

Examples:
Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
Output: [0,2,0,0,0]

Input: logs = [[1,1],[2,2],[2,3]], k = 4
Output: [1,1,0,0]

Problem source: LeetCode

Usage: find_users_active_minutes.py "id,ts id,ts, ..." <k>
"""

from typing import List
from utils import read_int_matrix
import sys

def finding_users_active_minutes(logs: List[List[int]], k: int) -> List[int]:
  user_minutes = {}

  for _id, ts in logs:
    if _id not in user_minutes:
      user_minutes[_id] = set([ts])
    else:
      user_minutes[_id].add(ts)

  uams = {}
  for minutes in user_minutes.values():
    uam = len(minutes)
    if uam not in uams:
      uams[uam] = 1
    else:
      uams[uam] += 1

  answer = [0] * k
  for j, uam in uams.items():
    answer[j-1] = uam

  return answer


if __name__ == "__main__":
  print(finding_users_active_minutes(read_int_matrix(sys.argv[1]), int(sys.argv[2])))
"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Examples:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from collections import deque

class RecentCounter:

  def __init__(self):
    self.last_requests = deque()

  def ping(self, t: int) -> int:
    self.last_requests.append(t)

    while t - self.last_requests[0] > 3000:
      self.last_requests.popleft() 

    return len(self.last_requests)
    

if __name__ == "__main__":
  pass
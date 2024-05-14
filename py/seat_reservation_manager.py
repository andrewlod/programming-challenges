"""
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

Examples:
Input
  ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
  [[5], [], [], [2], [], [], [], [], [5]]
Output
  [null, 1, 2, null, 2, 3, 4, 5, null]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from heapq import heapify, heappop, heappush

class SeatManager:

  def __init__(self, n: int):
    self.unreserved = [i+1 for i in range(n)]
    heapify(self.unreserved)

  def reserve(self) -> int:
    return heappop(self.unreserved)

  def unreserve(self, seatNumber: int) -> None:
    heappush(self.unreserved, seatNumber)

# Better solution
class SeatManager2:

  def __init__(self, n: int):
    self.released = []
    heapify(self.released)
    self.current_seat = 1

  def reserve(self) -> int:
    if self.released:
      return heappop(self.released)
    else:
      num = self.current_seat
      self.current_seat += 1
      return num

  def unreserve(self, seatNumber: int) -> None:
    heappush(self.released, seatNumber)
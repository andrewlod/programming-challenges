"""
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

Examples:
Input: tickets = [2,3,2], k = 2
Output: 6

Input: tickets = [5,1,1,1], k = 0
Output: 8

Problem source: LeetCode

Usage: time_needed_to_buy_tickets.py <comma_separated_tickets> <k>
"""

from typing import List
from utils import read_int_array
import sys

def time_required_to_buy(tickets: List[int], k: int) -> int:
  tickets_wanted = tickets[k]
  seconds_waited = 0

  for i, ticket in enumerate(tickets):
    if i > k and tickets_wanted <= ticket:
      seconds_waited += min(ticket, tickets_wanted) - 1
    else:
      seconds_waited += min(ticket, tickets_wanted)

  return seconds_waited


if __name__ == '__main__':
  print(time_required_to_buy(read_int_array(sys.argv[1]), int(sys.argv[2])))
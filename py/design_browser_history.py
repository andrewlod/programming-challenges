"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

Examples:
Input
  ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
  [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
  [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class DoublyLinkedNode:
  def __init__(self, val="", next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

class BrowserHistory:

  def __init__(self, homepage: str):
    self.history = DoublyLinkedNode(homepage)

  def visit(self, url: str) -> None:
    self.history.next = DoublyLinkedNode(val=url, prev=self.history)
    self.history = self.history.next

  def back(self, steps: int) -> str:
    for _ in range(steps):
      if not self.history.prev:
        return self.history.val

      self.history = self.history.prev

    return self.history.val

  def forward(self, steps: int) -> str:
    for i in range(steps):
      if not self.history.next:
        return self.history.val

      self.history = self.history.next

    return self.history.val
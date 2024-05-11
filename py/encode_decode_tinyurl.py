"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.

Examples:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

import random

class Codec:
  def __init__(self):
    self.short_to_long = {}
    self.choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

  def generate_id(self) -> str:
    _id = ""
    for _ in range(6):
      _id += random.choice(self.choices)

    return _id

  def encode(self, longUrl: str) -> str:
    """Encodes a URL to a shortened URL.
    """
    short_url = f"http://tinyurl.com/{self.generate_id()}"
    self.short_to_long[short_url] = longUrl

    return short_url
      

  def decode(self, shortUrl: str) -> str:
    """Decodes a shortened URL to its original URL.
    """
    return self.short_to_long.get(shortUrl, "")
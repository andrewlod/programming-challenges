"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Examples:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Problem source: LeetCode

Usage: defang_ip_address.py <address>
"""

import sys

def defang_ip_addr(address: str) -> str:
  return address.replace(".", "[.]")


if __name__ == "__main__":
  print(defang_ip_addr(sys.argv[1]))
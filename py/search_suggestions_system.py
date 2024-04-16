"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Examples:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Problem source: LeetCode

Usage: search_suggestions_system.py <comma_separated_strings> <search_word>
"""

from typing import List
from utils import read_str_array
import sys

def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
  result = []
  products = sorted(products)

  for i in range(1, len(search_word) + 1):
    word = search_word[0 : i]
    current_products = []
    for i, product in enumerate(products):
      if len(current_products) >= 3:
        break

      if product.startswith(word):
        current_products.append(product)

    result.append(current_products)

  return result


if __name__ == "__main__":
  print(suggested_products(read_str_array(sys.argv[1]), sys.argv[2]))
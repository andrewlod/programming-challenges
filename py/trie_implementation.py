"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Examples:
Input
  ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
  [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
  [null, null, true, false, true, null, true]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class Trie:

  def __init__(self):
    self.nodes = {}
    self.ends_word = False

  def _insert(self, word: str, idx: int) -> None:
    if idx >= len(word):
      self.ends_word = True
      return

    c = word[idx]
    if c not in self.nodes:
      self.nodes[c] = Trie()

    self.nodes[c]._insert(word, idx+1)

  def insert(self, word: str) -> None:
    if len(word) == 0:
      return True

    return self._insert(word, 0)

  def _search(self, word: str, idx: int, match_whole_word: bool) -> bool:
    if idx >= len(word):
      return not match_whole_word or match_whole_word and self.ends_word

    c = word[idx]
    if c not in self.nodes:
      return False

    return self.nodes[c]._search(word, idx+1, match_whole_word)

  def search(self, word: str) -> bool:
    if len(word) == 0:
      return True
    
    return self._search(word, 0, True)

  def starts_with(self, prefix: str) -> bool:
    return self._search(prefix, 0 , False)
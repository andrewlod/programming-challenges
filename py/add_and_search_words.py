"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Examples:
Input
  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
  [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
  [null,null,null,null,false,true,true,true]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class WordDictionary:

  def __init__(self):
    self.words = {}
    self.word_end = False

  def _add_word(self, word: str, idx: int):
    if idx >= len(word):
      self.word_end = True
      return

    char = word[idx]
    if char not in self.words:
      self.words[char] = WordDictionary()

    self.words[char]._add_word(word, idx+1)

  def addWord(self, word: str) -> None:
    self._add_word(word, 0)

  def _search(self, word: str, idx: int) -> bool:
    if idx >= len(word):
      return self.word_end
    
    if word[idx] == ".":
      for _, branch in self.words.items():
        if branch._search(word, idx + 1):
          return True
    else:
      if not word[idx] in self.words:
        return False

      return self.words[word[idx]]._search(word, idx+1)

    return False

  def search(self, word: str) -> bool:
    return self._search(word, 0)
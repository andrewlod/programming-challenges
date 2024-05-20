"""
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

Examples:
Input: answerKey = "TTFF", k = 2
Output: 4

Input: answerKey = "TFFT", k = 1
Output: 3

Input: answerKey = "TTFTTFTT", k = 1
Output: 5

Problem source: LeetCode

Usage: maximize_exam_confusion.py <answer_key> <k>
"""

from collections import deque
import sys

def maximize_count(answer_key: str, k: int, char: str) -> int:
  current_k = k
  current_count = 0
  sequence_count = 0
  max_count = 0
  sequences = deque([])
  for c in answer_key:
    if c == char:
      current_count += 1
      sequence_count += 1
      continue

    sequences.append(sequence_count)
    sequence_count = 0

    if current_k == 0:
      max_count = max(max_count, current_count)
      current_count -= sequences.popleft() + 1
      current_k += 1

    current_count += 1
    current_k -= 1

  return max(max_count, current_count)

def max_consecutive_answers(answerKey: str, k: int) -> int:
  return max(maximize_count(answerKey, k, 'T'), maximize_count(answerKey, k, 'F'))


if __name__ == '__main__':
  print(max_consecutive_answers(sys.argv[1], int(sys.argv[2])))
"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.


Examples:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Problem source: LeetCode

Usage: minimum_genetic_mutation.py <start_gene> <end_gene> <comma_separated_bank>
"""

from typing import List
from utils import read_str_array
import sys

def can_mutate_into(from_gene: str, to_gene: str) -> bool:
  mutations = 0
  for a, b in zip(from_gene, to_gene):
    if a != b:
      mutations += 1
      if mutations > 1:
        return False

  return mutations == 1

def min_mutation(startGene: str, endGene: str, bank: List[str]) -> int:
  if endGene not in bank:
    return -1
  
  if can_mutate_into(startGene, endGene) and endGene in bank:
    return 1

  connections = {
    startGene: []
  }

  for gene in bank:
    if can_mutate_into(startGene, gene):
      connections[startGene].append(gene)

  for i in range(len(bank)-1):
    for j in range(i+1, len(bank)):
      if can_mutate_into(bank[i], bank[j]):
        if not bank[i] in connections:
          connections[bank[i]] = [bank[j]]
        else:
          connections[bank[i]].append(bank[j])

        if not bank[j] in connections:
          connections[bank[j]] = [bank[i]]
        else:
          connections[bank[j]].append(bank[i])

  visited = set([])
  genes = [startGene]
  mutations = 0
  while genes and len(visited) < len(bank) + 1:
    new_genes = []

    for gene in genes:
      if gene in visited:
        continue

      if gene == endGene:
        return mutations
      
      visited.add(gene)
      if gene in connections:
        new_genes += connections[gene]

    mutations += 1
    genes = new_genes

  return -1


if __name__ == "__main__":
  print(min_mutation(sys.argv[1], sys.argv[2], read_str_array(sys.argv[3])))
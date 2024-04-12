from typing import List

def read_int_array(input: str) -> List[int]:
  return [int(val) for val in input.split(",")]


def read_int_matrix(input: str) -> List[List[int]]:
  return [
    [int(val) for val in item.split(",")] for item in input.split(" ")
  ]
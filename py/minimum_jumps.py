"""
This script calculates the minimum jumps required for a sequence of numbers, where each number
represents the maximum 'leap' distance allowed. For example, given an array arr = [4,9,2,3,4,5,1,1,1,1,1]
the starting number '4' means that the next leap can be to one of the following: 9, 2, 3 or 4.

Examples:
Input: 4,3,4,2,6,1,2,1
Output: 2

Input: 6,1,1,1,1,1,3
Output: 1

Input: 1,1,1,1
Output: 3

Input: 2,1
Output: 1

Input: 2,3,0,1,4
Output: 2

Problem source: Interview Pen (https://www.youtube.com/watch?v=yM9Xbi-MigE)

Usage: minimum_jumps.py <comma_separated_sequence>
"""

import sys

def do_jump(arr, index, start_index):
    """
    Finds the best possible jump index

    Parameters:
    arr (list[int]): Sequence of integers to calculate jumps
    index (int): Current index
    start_index (int): Index to start checks from

    Returns:
    Tuple(int, int): First integer represents the best possible jump index, while
    the second one represents the index to continue checks from.
    """
    current = arr[index]
    
    if index + current >= len(arr)-1:
        return (len(arr)-1, len(arr)-1)
        
    best_idx = index + current
    
    for i in range(start_index, index + current):
        num = i + arr[i]
        
        if num == 0:
          continue
        
        best_num = best_idx + arr[best_idx]
        
        if best_num >= len(arr)-1:
            return (best_idx, len(arr)-1)
            
        if num >= len(arr)-1:
            return (i, len(arr)-1)
        
        if num > best_num or arr[best_idx] == 0:
            best_idx = i
            
    
    return (best_idx, index + current)


def min_jumps(arr):
    """
    Calculates the minimum amount of jumps necessary to traverse the array

    Parameters:
    arr (list[int]): Sequence of integers to calculate jumps

    Returns:
    int: Minimum amount of jumps
    """
    idx = 0
    start_idx = 0
    jumps = 0
    
    while idx < len(arr)-1:
        idx, start_idx = do_jump(arr, idx, start_idx+1)
        jumps += 1
      
    return jumps
    

if __name__ == "__main__":
    print(min_jumps(
        [int(value) for value in sys.argv[1].split(",")]
    ))
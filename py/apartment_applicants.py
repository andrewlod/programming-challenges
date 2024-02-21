"""
This script calculates how many apartment applicants would have a matching apartment according to their price requirements given a range k.

Examples:
Input: 60,45,80,60 30,75,60 5
Output: 2

Problem source: Interview Pen (https://www.youtube.com/watch?v=QvqvMxg24gY)

Usage: apartment_applicants.py <applicants_requirements> <apartment_prices> <acceptable_range>
"""

import sys

def binary_search(sorted_array: list[int], goal: int, k: int) -> bool:
    """
    Performs binary search (O(log n)) to find the goal within a given range.

    Parameters:
    sorted_array (list[int]): Sorted array of int values
    goal (int): Value to be search
    k (int): Tolerance range - Values within k range of the goal (exclusive) will be accepted

    Returns:
    bool: Whether the number within the k range of the goal was found
    """
    start = 0
    end = len(sorted_array) - 1

    while start <= end:
        midpoint = (start + end) // 2

        value = sorted_array[midpoint]
        if value - k < goal < value + k:
            return True
    
        if value > goal:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return False


def num_satisfied_applicants(applicants: list[int], apartments: list[int], k: int) -> int:
    """
    Calculates how many applicants have a matching apartment. P.S.: Multiple applicants can be matched with the same apartment.

    Parameters:
    applicants (list[int]): List of applicant bids
    apartments (list[int]): List of apartment values
    k (int): Tolerance range - Values within k range of a given bid (exclusive) will be accepted

    Returns:
    int: Number of matching applicants
    """
    apartments.sort()

    matches = 0
    for applicant in applicants:
        if binary_search(apartments, applicant, k):
            matches += 1

    return matches

if __name__ == "__main__":
    print(num_satisfied_applicants(
        [int(item) for item in sys.argv[1].split(',')], 
        [int(item) for item in sys.argv[2].split(',')], 
        int(sys.argv[3])
    ))

//! This module was written to solve the "Summary Ranges" problem from LeetCode.
//!
//! You are given a sorted unique integer array nums.
//! 
//! A range [a,b] is the set of all integers from a to b (inclusive).
//! 
//! Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
//! 
//! Each range [a,b] in the list should be output as:
//! 
//! "a->b" if a != b
//! "a" if a == b
//! 
//! Examples:
//! Input: nums = [0,1,2,4,5,7]
//! Output: ["0->2","4->5","7"]
//! 
//! Input: nums = [0,2,3,4,6,8,9]
//! Output: ["0","2->4","6","8->9"]
//! 
//! Usage: summary_ranges(nums)

fn push_range(ranges: &mut Vec<String>, first: i32, last: i32) {
  if first == last {
    ranges.push(format!("{}", &first));
  } else {
    ranges.push(format!("{}->{}", &first, &last));
  }
}

pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
  if nums.is_empty() {
    return vec![];
  }

  let mut ranges: Vec<String> = Vec::new();

  let mut first = nums[0];
  let mut last = nums[0];

  for item in nums.into_iter().skip(1) {
    if item - 1 != last {
      push_range(&mut ranges, first, last);
      first = item;
    }

    last = item;
  }

  push_range(&mut ranges, first, last);

  ranges
}
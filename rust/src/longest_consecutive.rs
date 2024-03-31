//! This module was written to solve the "Longest Consecutive Sequence" problem from LeetCode.
//!
//! Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
//! 
//! Examples:
//! Input: nums = [100,4,200,1,3,2]
//! Output: 4
//! 
//! Input: nums = [0,3,7,2,5,8,4,6,0,1]
//! Output: 9
//! 
//! Usage: longest_consecutive(nums)

use std::collections::HashSet;

pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
  if nums.is_empty() {
    return 0;
  }

  let nums_set: HashSet<i32> = nums.into_iter().collect();
  let mut max_len = 1;

  for &item in &nums_set {
    if !nums_set.contains(&(item - 1)) {
      let count = (item..).take_while(|val| nums_set.contains(val)).count();
      max_len = max_len.max(count);
    }
  }

  max_len as i32
}
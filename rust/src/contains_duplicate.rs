//! This module was written to solve the "Contains Duplicate" problem from LeetCode.
//!
//! Given an integer array `nums` and an integer `k, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.
//! 
//! Examples:
//! Input: nums = [1,2,3,1], k = 3
//! Output: true
//! 
//! Input: nums = [1,2,3,1,2,3], k = 2
//! Output: false
//! 
//! Usage: contains_nearby_duplicate(nums, k)

use std::collections::HashMap;

/// Determines if there is a number with a duplicate within `k` range
pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
  let mut last_indexes: HashMap<i32, u32> = HashMap::new();

  for (i, num) in nums.into_iter().enumerate() {
    let idx = i as u32;
    match last_indexes.get(&num) {
      Some(v) => {
        if i32::abs((idx - v) as i32) <= k {
            return true;
        }
        last_indexes.insert(num, idx);
      }
      None => {
        last_indexes.insert(num, idx);
      }
    }
  }

  false
}
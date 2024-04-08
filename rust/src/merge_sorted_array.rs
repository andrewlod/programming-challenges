//! This module was written to solve the "Merge Sorted Array" problem from LeetCode.
//!
//! You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
//! 
//! Merge nums1 and nums2 into a single array sorted in non-decreasing order.
//! 
//! The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
//! 
//! Examples:
//! Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
//! Output:[1,2,2,3,5,6]
//! 
//! Input: nums1 = [0], m = 0, nums2 = [1], n = 1
//! Output: [1]
//! 
//! Usage: merge(nums1, m, nums2, n)

pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
  let m = m as usize;
  let n = n as usize;
  let mut nums3: Vec<i32> = vec![0i32; m + n];

  let mut ptr_1 = 0usize;
  let mut ptr_2 = 0usize;
  let mut ptr_3 = 0usize;

  while ptr_1 < m || ptr_2 < n {
    if ptr_2 >= n || (ptr_1 < m && nums1[ptr_1] < nums2[ptr_2]) {
      nums3[ptr_3] = nums1[ptr_1];
      ptr_1 += 1;
    } else {
      nums3[ptr_3] = nums2[ptr_2];
      ptr_2 += 1;
    }

    ptr_3 += 1;
  }

  *nums1 = nums3;
}
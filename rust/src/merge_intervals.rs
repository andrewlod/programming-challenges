//! This module was written to solve the "Merge Intervals" problem from LeetCode.
//!
//! Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
//! 
//! Examples:
//! Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
//! Output: [[1,6],[8,10],[15,18]]
//! 
//! Input: intervals = [[1,4],[4,5]]
//! Output: [[1,5]]
//! 
//! Usage: merge(intervals)

use std::cmp::max;

/// Merges intervals in a vector of intervals
pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
  let mut intervals_copy = intervals.clone();
  intervals_copy.sort_by(|a, b| {
    a[0].cmp(&b[0])
  });

  let mut intervals_iter = intervals_copy.into_iter();
  let first = intervals_iter.next().unwrap();
  let mut merged = vec![first];

  for interval in intervals_iter {
    let current = merged.last_mut().unwrap();

    if current[1] >= interval[0] {
      current[1] = max(current[1], interval[1]);
    } else {
      merged.push(interval);
    }
  }

  merged
}
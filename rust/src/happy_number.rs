//! This module was written to solve the "Happy Number" problem from LeetCode.
//!
//! A number is a happy number if:
//! - Starting with any positive integer, replace the number by the sum of the squares of its digits.
//! - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
//! - Those numbers for which this process ends in 1 are happy.
//! 
//! Examples:
//! Input: n = 19
//! Output: true
//! Explanation:
//! 1² + 9² = 82
//! 8² + 2² = 68
//! 6² + 8² = 100
//! 1² + 0² + 0² = 1
//! 
//! Input: 2
//! Output: false
//! 
//! Usage: is_happy(n)

use std::collections::HashSet;

/// Gets the sum of the squares of a given number's digits.
fn get_sum_of_squares(n: u32) -> u32 {
  let str_n = n.to_string();

  let digits = str_n.chars().map(|d| d.to_digit(10).unwrap());

  digits.into_iter().fold(0, |acc, a| {
    acc + a.pow(2)
  })
}

/// Determines whether a number is a happy number or not
pub fn is_happy(n: i32) -> bool {
  if n == 1 {
    return true;
  }

  let mut squares: HashSet<u32> = HashSet::new();
  let mut last_sum = n as u32;
  squares.insert(last_sum);

  while last_sum != 1 {
    last_sum = get_sum_of_squares(last_sum);
    if squares.contains(&last_sum) {
      return false;
    }

    squares.insert(last_sum);
  }

  true
}
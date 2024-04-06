//! This module was written to solve the "Valid Parentheses" problem from LeetCode.
//!
//! Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//! 
//! An input string is valid if:
//! 
//! - Open brackets must be closed by the same type of brackets.
//! - Open brackets must be closed in the correct order.
//! - Every close bracket has a corresponding open bracket of the same type.
//! 
//! Examples:
//! Input: s = "()"
//! Output: true
//! 
//! Input: "(]"
//! Output: false
//! 
//! Usage: is_valid(s)

use std::collections::HashMap;

const OPENING_CHARACTERS: &[char] = &['(', '[', '{'];

/// Checks if the current character is an opening character - (, [ or {
fn is_opening_character(c: &char) -> bool {
  OPENING_CHARACTERS.contains(c)
}

/// Checks if the given sequence of parenthesis, braces and brackets is valid
pub fn is_valid(s: String) -> bool {
  let closing_characters: HashMap<char, char> = [
    (')', '('),
    (']', '['),
    ('}', '{')
  ].iter().copied().collect();

  let mut stack: Vec<char> = vec![];

  for character in s.chars() {
      if is_opening_character(&character) {
        stack.push(character);
        continue;
      }

      let popped = stack.pop();

      match popped {
        Some(c) => {
          if closing_characters.get(&character).unwrap_or(&'.') != &c {
            return false;
          }
        },
        None => return false
      }
  }

  stack.is_empty()
}
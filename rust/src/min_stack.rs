//! This module was written to solve the "Min Stack" problem from LeetCode.
//!
//! Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
//! 
//! Implement the MinStack class:
//! 
//! - MinStack() initializes the stack object.
//! - void push(int val) pushes the element val onto the stack.
//! - void pop() removes the element on the top of the stack.
//! - int top() gets the top element of the stack.
//! - int getMin() retrieves the minimum element in the stack.
//! You must implement a solution with O(1) time complexity for each function.
//! 
//! Examples:
//! let min_stack = MinStack::new();
//! min_stack.push(-2);
//! min_stack.push(0);
//! min_stack.push(-3);
//! min_stack.get_min(); // return -3
//! min_stack.pop();
//! min_stack.top();    // return 0
//! min_stack.get_min(); // return -2

use std::cmp::min;

struct StackElement {
  min: Option<i32>,
  value: i32
}

struct MinStack {
  min_value: Option<i32>,
  data: Vec<StackElement>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {
  fn new() -> Self {
    Self { min_value: None, data: vec![] }
  }
  
  fn push(&mut self, val: i32) {
    let top = StackElement{min: self.min_value, value: val};
    self.min_value = Some(min(self.get_min(), val));
    self.data.push(top);
  }
  
  fn pop(&mut self) {
    let deleted = self.data.pop();
    self.min_value = deleted.unwrap().min;
  }
  
  fn top(&self) -> i32 {
    self.data.last().unwrap().value
  }
  
  fn get_min(&self) -> i32 {
      match self.min_value {
        Some(v) => return v,
        None => return i32::MAX
      }
  }
}
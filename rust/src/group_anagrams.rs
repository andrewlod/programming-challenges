//! This module was written to solve the "Group Anagrams" problem from LeetCode.
//!
//! Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
//! 
//! Examples:
//! Input: strs = ["eat","tea","tan","ate","nat","bat"]
//! Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//! 
//! Input: strs = [""]
//! Output: [[""]]
//! 
//! Usage: group_anagrams(strs)

use std::collections::{BinaryHeap, HashMap};

/// Groups anagrams within a list of string values using HeapSorted char Vecs as keys for grouping the anagrams
pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
  let mut hash_groups: HashMap<Vec<char>, Vec<String>> = HashMap::new();

  for ele in strs {
    let ele_col: BinaryHeap<char> = ele.chars().collect();
    let sorted_ele = ele_col.into_sorted_vec();

      match hash_groups.get_mut(&sorted_ele) {
          Some(val) => {
            let ele_clone = ele.clone();
            val.push(ele_clone);
          },
          None => {
            let ele_clone = ele.clone();
            hash_groups.insert(sorted_ele, vec![ele_clone]);
          }
      }
  }

  hash_groups.into_values().collect()
}
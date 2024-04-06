//! This module was written to solve the "Simplify Path" problem from LeetCode.
//!
//! Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
//! 
//! In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
//! 
//! The canonical path should have the following format:
//! 
//! - The path starts with a single slash '/'.
//! - Any two directories are separated by a single slash '/'.
//! - The path does not end with a trailing '/'.
//! - The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
//! 
//! Return the simplified canonical path.
//! 
//! Examples:
//! Input: path = "/home/"
//! Output: "/home"
//! 
//! Input: path = "/home//foo/"
//! Output: "/home/foo"
//! 
//! Usage: simplify_path(path)

/// Simplifies an OS path, removing `..`, `.` and `//`
pub fn simplify_path(path: String) -> String {
  let paths = path.split('/').skip(1);

  let mut simplified_path: Vec<&str> = vec![];

  for element in paths {
      if element.is_empty() || element == "." {
        continue;
      }

      if element == ".." {
        simplified_path.pop();
        continue;
      }

      simplified_path.push(element);
  }

  format!("/{}", simplified_path.join("/"))
}
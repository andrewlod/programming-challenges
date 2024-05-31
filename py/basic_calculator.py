"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Examples:
Input: s = "1 + 1"
Output: 2

Input: s = " 2-1 + 2 "
Output: 3

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Problem source: LeetCode

Usage: basic_calculator.py <s>
"""

operations = {
  "+": lambda a, b: a + b,
  "-": lambda a, b: a - b
}

def evaluate_expr(self, s: str) -> int:
    current_expr = []
    parenthesis_stack = 0
    nested_expression = False
    current_val = 0
    current_num = 0
    current_operation = operations["+"]
    for c in s:
      if c == "(":
        if parenthesis_stack > 0:
          current_expr.append(c)

        parenthesis_stack += 1
        nested_expression = True
        continue
      elif c == ")":
        parenthesis_stack -= 1
        if parenthesis_stack > 0:
          current_expr.append(c)

        if parenthesis_stack == 0:
          current_num = self.evaluate_expr("".join(current_expr))
          current_expr = []
          nested_expression = False

        continue
      
      if nested_expression:
        current_expr.append(c)
        continue

      if c.isdigit():
        current_num = current_num * 10 + int(c)
      else:
        current_val = current_operation(current_val, current_num)
        current_operation = operations[c]
        current_num = 0

    return current_operation(current_val, current_num)

def calculate(self, s: str) -> int:
  sanitized_str = s.strip().replace(" ", "")
  return self.evaluate_expr(sanitized_str)
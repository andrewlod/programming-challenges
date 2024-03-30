use std::collections::HashSet;

fn get_sum_of_squares(n: u32) -> u32 {
  let str_n = n.to_string();

  let digits = str_n.chars().map(|d| d.to_digit(10).unwrap());

  digits.into_iter().fold(0, |acc, a| {
    acc + a.pow(2)
  })
}

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
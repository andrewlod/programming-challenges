//! This module was written to solve the "Coin Change" problem from LeetCode.
//!
//! You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
//! 
//! Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
//! 
//! You may assume that you have an infinite number of each kind of coin.
//! 
//! Examples:
//! Input: coins = [1,2,5], amount = 11
//! Output: 3
//! 
//! Input: coins = [2], amount = 3
//! Output: -1
//! 
//! Input: coins = [1], amount = 0
//! Output: 0
//! 
//! Usage: coin_change(coins, amount)

pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
  if amount == 0 {
    return 0;
  }
  
  let mut dp: Vec<i32> = vec![amount + 1; amount as usize + 1];
  dp[0] = 0;
  
  for i in 1..=amount as usize {
    for coin in coins.iter() {
      let idx = i as i32;
      if *coin == idx {
        dp[i] = 1;
        continue;
      }

      if idx % coin == 0 {
        dp[i] = dp[i].min(idx / coin);
      }

      if *coin < idx {
        dp[i] = dp[i].min(1 + dp[i - *coin as usize]);
      }
    }
  }

  let result = dp[amount as usize];
  if result > amount {
    return -1
  }

  result
}
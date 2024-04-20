"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Examples:
Input: senate = "RD"
Output: Radiant

Input: senate = "RDD"
Output: Dire

Problem source: LeetCode

Usage: dota2_senate.py <senate>
"""
import sys

def find_next(senate: str, team: str, banned: set, index: int) -> int:
  for i in range(index, len(senate)):
    if senate[i] == team and i not in banned:
      return i

  for i in range(0, index):
    if senate[i] == team and i not in banned:
      return i

  return -1

def predict_party_victory(senate: str) -> str:
  n = len(senate)
  radiants = set()
  dires = set()

  banned = set()

  for i, senator in enumerate(reversed(senate)):
    if senator == "R":
      radiants.add(n-i-1)
    else:
      dires.add(n-i-1)

  while len(radiants) > 0 and len(dires) > 0:
    for i, senator in enumerate(senate):
      if len(radiants) == 0 or len(dires) == 0:
        break

      if i in banned:
        continue

      if senator == "R":
        idx = find_next(senate, "D", banned, i + 1)

        if idx == -1:
          continue

        dires.remove(idx)
        banned.add(idx)
      else:
        idx = find_next(senate, "R", banned, i + 1)
        
        if idx == -1:
          continue

        radiants.remove(idx)
        banned.add(idx)

  if len(radiants) > len(dires):
    return "Radiant"
  
  return "Dire"


if __name__ == "__main__":
  print(predict_party_victory(sys.argv[1]))
#include <iostream>
#include <string>

using namespace std;

int trailingZeroes(int n) {
  int total = 0;
  int multiplier = 5;

  while (n / multiplier > 0) {
      total += n / multiplier;
      multiplier *= 5;
  }

  return total;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: factorial_trailing_zeroes <n>" << endl;
        return 1;
    }
    cout << trailingZeroes(stoi(argv[1])) << endl;
    return 0;
}
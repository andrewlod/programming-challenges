#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

int rangeBitwiseAnd(int left, int right) {
    int shifts = 0;
    while (left != right) {
        left >>= 1;
        right >>= 1;
        shifts++;
    }
    return left << shifts;
}

int main(int argc, char const *argv[])
{
    if (argc != 3) {
        cout << "Usage: bitwise_and_of_numbers_range <left> <right>" << endl;
        return 1;
    }
    cout << rangeBitwiseAnd(stoi(argv[1]), stoi(argv[2])) << endl;
    return 0;
}
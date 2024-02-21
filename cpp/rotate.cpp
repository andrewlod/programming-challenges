#include <iostream>
#include <vector>
#include <unordered_set>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Rotates a given vector for `k` places.
 *
 * @param nums Vector to be rotated
 * @param k Amount of places to rotate
 */
void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    if (k == 0 || k % n == 0)
        return;

    unordered_set<int> visitedIdx;
    k = k % n;

    int firstNumber, aux;
    for (int i = 0; i < n; i++) {
        if (visitedIdx.find(i) != visitedIdx.end())
            continue;
        firstNumber = nums[i];

        int j = (i + k) % n;
        while (visitedIdx.find(j) == visitedIdx.end()) {
            visitedIdx.insert(j);
            
            aux = nums[j];
            nums[j] = firstNumber;
            firstNumber = aux;

            j = (j + k) % n;
        }
    }
}

int main(int argc, char const *argv[])
{
    if (argc != 3) {
        cout << "Usage: rotate <comma_separated_values> <k>" << endl;
        return 1;
    }
    auto nums = splitToInt(argv[1]);
    rotate(nums, stoi(argv[2]));
    printVector(nums);

    return 0;
}
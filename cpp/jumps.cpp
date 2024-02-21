#include <iostream>
#include <vector>
#include <unordered_map>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Does a single step of jump, finding the best index to jump to.
 *
 * @param nums Vector containing jump data
 * @param currentIdx Current jump index
 * @param startIdx Index to start looking for best jumps
 * @return Index of the best jump possible and index to start next iteration.
 */
pair<int,int> doJump(const vector<int>& nums, int currentIdx, int startIdx) {
    int max = currentIdx + nums[currentIdx];

    if (max >= nums.size() - 1)
        return make_pair(max, nums.size() - 1);

    int best = max + nums[max];
    int bestIdx = max;

    for (int i = startIdx; i < best; i++) {
        int target = i + nums[i];

        if (target >= nums.size() - 1)
            return make_pair(i, nums.size() - 1);

        if (target > best) {
            best = target;
            bestIdx = i;
        }
    }

    return make_pair(bestIdx, max);
}

/**
 * Calculates whether it is possible to traverse the vector where each element represents the maximum jump length.
 *
 * @param nums Vector containing jump data
 * @return Whether it is possible to traverse the vector.
 */
bool canJump(const vector<int>& nums) {
    int currentIdx = 0;
    int lastIdx = 0;

    while (currentIdx < nums.size()-1) {
        auto bestJump = doJump(nums, currentIdx, lastIdx);

        if (bestJump.first == currentIdx)
            return false;

        currentIdx = bestJump.first;
        lastIdx = bestJump.second;
    }

    return true;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: jump <comma_separated_values>" << endl;
        return 1;
    }
    cout << canJump(splitToInt(argv[1])) << endl;
    return 0;
}

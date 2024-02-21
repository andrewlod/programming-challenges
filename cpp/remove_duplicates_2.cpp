#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Removes duplicates from a vector, but up to one duplicate is allowed.
 *
 * @param nums Vector with duplicate values
 * @return New size of the vector.
 */
int removeDuplicates(vector<int>& nums) {
    int idx = 0;
    int lastCount = 1;

    for (int i = 1; i < nums.size(); i++) {
        if (nums[idx] != nums[i]) {
            lastCount = 1;
            idx++;
            nums[idx] = nums[i];
            continue;
        }

        lastCount++;
        if (lastCount <= 2) {
            idx++;
            nums[idx] = nums[i];
        }
    }

    return idx + 1;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: remove_duplicates_2 <comma_separated_values>" << endl;
        return 1;
    }
    cout << removeDuplicates(splitToInt(argv[1])) << endl;
    return 0;
}
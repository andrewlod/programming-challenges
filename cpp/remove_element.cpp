#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Removes all occurrences of a given element from a vector.
 *
 * @param nums Vector to remove an element from
 * @param val Value to be removed
 * @return New size of the vector.
 */
int removeElement(vector<int>& nums, int val) {
    int lastIdx = nums.size()-1;

    for (int i = 0; i <= lastIdx; i++) {
        if (nums[i] != val)
            continue;

        while (nums[lastIdx] == val) {
            if (lastIdx == 0)
                return 0;
            lastIdx--;
        }

        if (i > lastIdx)
            return lastIdx + 1;

        nums[i] = nums[lastIdx];
        lastIdx--;
    }

    return lastIdx + 1;
}

int main(int argc, char const *argv[])
{
    if (argc != 3) {
        cout << "Usage: remove_element <comma_separated_values> <value_to_remove>" << endl;
        return 1;
    }
    cout << removeElement(splitToInt(argv[1]), stoi(argv[2])) << endl;
    return 0;
}
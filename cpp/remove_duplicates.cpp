#include <iostream>
#include <vector>
#include <unordered_set>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Removes duplicates from a vector.
 *
 * @param nums Vector with duplicate values
 * @return New size of the vector.
 */
int removeDuplicates(vector<int>& nums) {
    unordered_set<int> foundNums;

    int idx = 0;
    for (int i = 0; i < nums.size(); i++) {
        int num = nums[i];
        if (foundNums.find(num) != foundNums.end()) 
            continue;

        foundNums.insert(num);
        nums[idx] = num;
        idx++;
    }

    return idx;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: remove_duplicates <comma_separated_values>" << endl;
        return 1;
    }
    cout << removeDuplicates(splitToInt(argv[1])) << endl;
    return 0;
}
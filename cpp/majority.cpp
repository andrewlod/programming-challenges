#include <iostream>
#include <vector>
#include <unordered_map>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Calculates the majority element. The majority element count is always greater than n/2, where n is the vector size.
 *
 * @param nums Vector of elements
 * @return Majority element of the vector.
 */
int majorityElement(const vector<int>& nums) {
    unordered_map<int,int> counts;

    int majorityNum;
    int maxCount = 0;

    for (int i = 0; maxCount < nums.size() / 2 + 1; i++) {
        int num = nums[i];
        counts[num]++;

        int count = counts[num];
        if (count > maxCount) {
            maxCount = count;
            majorityNum = num;
        }
    }

    return majorityNum;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: majority <comma_separated_values>" << endl;
        return 1;
    }
    cout << majorityElement(splitToInt(argv[1])) << endl;
    return 0;
}

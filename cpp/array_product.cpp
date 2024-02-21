#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Returns a vector where each element is equal to the product of the original vector except itself.
 *
 * @param nums Vector of integers
 * @return Vector of products of each element except itself.
 */
vector<int> productExceptSelf(const vector<int>& nums) {
    int product = 1;
    vector<int> answer(nums.size());
    bool hasZero = false;
    bool hasMultipleZeroes = false;

    for (auto& num : nums) {
        if (num == 0) {
            if (hasZero)
                hasMultipleZeroes = true;
            hasZero = true;
            continue;
        }

        product *= num;
    }

    for (int i = 0; i < nums.size(); i++) {
        if (hasMultipleZeroes)
            answer[i] = 0;
        else if (hasZero) {
            answer[i] = nums.at(i) == 0 ? product : 0;
        } else {
            answer[i] = product / nums.at(i);
        }
    }

    return answer;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: array_product <comma_separated_values>" << endl;
        return 1;
    }
    auto vec = productExceptSelf(splitToInt(argv[1]));
    printVector(vec);
    return 0;
}

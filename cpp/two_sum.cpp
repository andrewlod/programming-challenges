#include <iostream>
#include <vector>
#include <unordered_map>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Finds a pair of values that sum up to a given target.
 *
 * @param numbers Vector of integers, where 2 of the elements add up to target
 * @param target Target number
 * @return New size of the vector.
 */
vector<int> twoSum(const vector<int>& numbers, int target) {
    unordered_map<int, int> numIdx;
    std::vector<int> answer;

    numIdx[numbers[0]] = 0;

    for (int i = 1; i < numbers.size(); i++) {
        int num = numbers[i];
        if (numIdx.count(target-num)) {
            answer.push_back(numIdx[target-num] + 1);
            answer.push_back(i + 1);
            break;
        }

        numIdx[numbers[i]] = i;
    }

    return answer;
}

int main(int argc, char const *argv[])
{
    if (argc != 3) {
        cout << "two_sum <comma_separated_values> <target>" << endl;
        return 1;
    }
    auto result = twoSum(splitToInt(argv[1]), stoi(argv[2]));
    printVector(result);
    
    return 0;
}
#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Merges two sorted vectors. Nums1 becomes the merged array
 *
 * @param nums1 First sorted vector of elements
 * @param m Number of elements in the first vector
 * @param nums2 Second sorted vector of elements
 * @param n Number of elements in the second vector
 */
void merge(vector<int>& nums1, int m, const vector<int>& nums2, int n) {
    vector<int> merged;
    unsigned int idx1 = 0;
    unsigned int idx2 = 0;

    while (idx1 < m || idx2 < n) {
        if ((idx2 >= n) || (idx1 < m && nums1[idx1] < nums2[idx2])) {
            merged.push_back(nums1[idx1]);
            idx1++;
        } else {
            merged.push_back(nums2[idx2]);
            idx2++;
        }
    }

    nums1 = merged;
}

int main(int argc, char const *argv[])
{
    if (argc != 3) {
        cout << "Usage: merge <comma_separated_sorted_array_1> <comma_separated_sorted_array_2>" << endl;
        return 1;
    }
    auto nums1 = splitToInt(argv[1]);
    auto nums2 = splitToInt(argv[2]);
    merge(nums1, nums1.size(), nums2, nums2.size());
    printVector(nums1);

    return 0;
}

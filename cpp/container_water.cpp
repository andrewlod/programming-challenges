#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Calculates the area of an interval of the vector.
 *
 * @param height Vector containing height values
 * @param left Left bound of the array
 * @param right Right bound of the array
 * @return Total area of the interval.
 */
int calculateArea(const vector<int>& height, int left, int right) {
    return min(height.at(left), height.at(right)) * (right-left);
}

/**
 * Calculates the maximum area of a vector of heights.
 *
 * @param height Vector containing height values
 * @return Maximum area possible.
 */
int maxArea(const vector<int>& height) {
    int max = 0;
    int left = 0;
    int right = height.size()-1;

    while (left < right) {
        int area = calculateArea(height, left, right);

        if (area > max)
            max = area;

        if (height.at(left) < height.at(right))
            left++;
        else
            right--;
    }

    return max;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: container_water <comma_separated_values>" << endl;
        return 1;
    }
    cout << maxArea(splitToInt(argv[1])) << endl;
    return 0;
}
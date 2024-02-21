#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Calculates the max profit possible given an array of prices. It is possible to buy and sell on the same day.
 *
 * @param prices Vector of prices
 * @return Maximum possible profit.
 */
int maxProfit(const vector<int>& prices) {
    int sum = 0;
    int localMin = prices[0];
    int localMax = prices[0];
    
    for (int i = 1; i < prices.size(); i++) {
        int currentPrice = prices[i];
        int previousPrice = prices[i-1];

        if (currentPrice > previousPrice) {
            sum += currentPrice - previousPrice;
        }
    }

    return sum;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: profit_2 <comma_separated_values>" << endl;
        return 1;
    }
    cout << maxProfit(splitToInt(argv[1])) << endl;
    return 0;
}

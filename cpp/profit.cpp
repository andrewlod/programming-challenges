#include <iostream>
#include <vector>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Calculates the max profit possible given an array of prices.
 * Constraint: it is only possible to buy and sell once.
 *
 * @param prices Vector of prices
 * @return Maximum possible profit for a single buy-sell operation.
 */
int maxProfit(const vector<int>& prices) {
    int best = 0;
    int min = prices[0];

    for (int i = 1; i < prices.size(); i++) {
        int price = prices[i];
        if (price < min) {
            min = price;
        }

        int current = price - min;
        if (current > best) {
            best = current;
        }
    }

    return best;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: profit <comma_separated_values>" << endl;
        return 1;
    }
    cout << maxProfit(splitToInt(argv[1])) << endl;
    return 0;
}

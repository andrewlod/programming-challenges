#include <unordered_map>
#include <string>
#include <iostream>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

const unordered_map<int, char> basicDigits = {
    {3, 'M'},
    {2, 'C'},
    {1, 'X'},
    {0, 'I'}
};

const unordered_map<int, char> fiveDigits = {
    {2, 'D'},
    {1, 'L'},
    {0, 'V'}
};

/**
 * Converts a number digit to its roman equivalent given its order.
 *
 * @param order Order of the digit, equivalent floor(log10(number))
 * @param digit Current digit of the number
 * @return Roman equivalent of the number digit.
 */
string digitToRoman(int order, int digit) {
    if (digit == 0)
        return "";

    if (digit == 4) {
        return string(1, basicDigits.at(order)) + string(1, fiveDigits.at(order));
    }

    if (digit == 9) {
        return string(1, basicDigits.at(order)) + string(1, basicDigits.at(order+1));
    }

    if (digit >= 5) {
        return string(1, fiveDigits.at(order)) + string(digit-5, basicDigits.at(order));
    }

    return string(digit, basicDigits.at(order));

}

/**
 * Converts an integer to a roman number.
 *
 * @param num Number to be converted to roman
 * @return Roman equivalent of the given number.
 */
string intToRoman(int num) {
    int order = 3;
    int divisor = 1000;
    string roman = "";

    while (num > 0) {
        int digit = num / divisor;
        roman += digitToRoman(order, digit);

        num = num % divisor;
        divisor /= 10;
        order--;
    }

    return roman;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: int_to_roman <integer_value>" << endl;
        return 1;
    }
    cout << intToRoman(stoi(argv[1])) << endl;
    return 0;
}
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <unordered_map>
#include "util/util.hpp"

using namespace std;

const vector<string> sub20 = {
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
};

const unordered_map<int, string> sub100 = {
    {2, "Twenty"},
    {3, "Thirty"},
    {4, "Forty"},
    {5, "Fifty"},
    {6, "Sixty"},
    {7, "Seventy"},
    {8, "Eighty"},
    {9, "Ninety"}
};

/**
 * Converts a number below 100 into its English equivalent.
 *
 * @param value Number lower than 100
 * @return English words representing the given number.
 */
string getNameBelow100(int value) {
    if (value == 0)
        return "";

    if (value < 20)
        return sub20[value-1];

    int lowestUnit = value % 10;
    int dozenUnit = value / 10;

    return lowestUnit == 0 ? sub100.at(dozenUnit) : sub100.at(dozenUnit) + " " + sub20.at(lowestUnit - 1);
}

/**
 * Gets the English equivalent of the power of 1000 place of a number. Example: 2147483647 -> "Billion", 1234 -> "Thousand"
 *
 * @param power Power of the number, equivalent to floor(log10(number))
 * @return English word representing whether the number if in the Thousands, Millions, Billions or none of them.
 */
string getNamePowerOf10(int power) {
    switch (power) {
        case 3: return "Thousand";
        case 6: return "Million";
        case 9: return "Billion";
        default: return "";
    }
}

/**
 * Converts any 32-bit integer into its English equivalent.
 *
 * @param num Number to be converted
 * @return English representation of the given number.
 */
string numberToWords(int num) {
    if (num == 0)
        return "Zero";

    int order = 9;
    int divisor = 1000000000;
    vector<string> englishWords;

    for (;num > 0; order-=3, num = num % divisor, divisor /= 1000) {
        int valueBelow1000 = num / divisor;
        if (valueBelow1000 == 0) {
            continue;
        }

        string powerOf10Name = getNamePowerOf10(order);
        
        if (valueBelow1000 >= 100) {
            int hundredDigit = valueBelow1000 / 100;
            englishWords.push_back(sub20[hundredDigit-1]);
            englishWords.push_back("Hundred");
            valueBelow1000 = valueBelow1000 % 100;
        }

        string belowHundredName = getNameBelow100(valueBelow1000);

        if (belowHundredName.size())
            englishWords.push_back(belowHundredName);
        
        if (powerOf10Name.size())
            englishWords.push_back(powerOf10Name);
        
    }

    string english = "";
    for (int i = 0; i < englishWords.size() - 1; i++)
        english += englishWords[i] + " ";
    
    english += englishWords[englishWords.size()-1];

    return english;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: int_to_english <integer_value>" << endl;
        return 1;
    }
    cout << numberToWords(stoi(argv[1])) << endl;
    return 0;
}
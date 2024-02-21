#include <iostream>
#include <string>

#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Checks if a character is alphanumeric.
 *
 * @param c Character to be checked
 * @return Whether the character is alphanumeric or not.
 */
bool isAlphanumeric(char c) {
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
}

/**
 * Checks if a string is a palindrome, ignoring non-alphanumeric characters.
 *
 * @param s String to be checked.
 * @return Whether the string is a palindrome or not.
 */
bool isPalindrome(const string& s) {
    unsigned int left = 0;
    unsigned int right = s.size()-1;
    
    while(left < right) {
        if (!isAlphanumeric(s[left])) {
            left++;
            continue;
        }

        if (!isAlphanumeric(s[right])) {
            right--;
            continue;
        }

        if (tolower(s[left]) != tolower(s[right]))
            return false;

        left++;
        right--;
    }

    return true;
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        cout << "Usage: palindrome <text>" << endl;
        return 1;
    }
    cout << isPalindrome(argv[1]) << endl;
    return 0;
}

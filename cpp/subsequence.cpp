#include <iostream>
#include <string>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * Checks if a given string `s` is a subsequence of the string `t`.
 *
 * @param s Substring
 * @param t Main string
 * @return New size of the vector.
 */
bool isSubsequence(const string& s, const string& t) {
    if (s.size() == 0)
        return true;

    unsigned int sPtr = 0;

    for (int i = 0; i < t.size(); i++) {
        if (t[i] == s[sPtr])
            sPtr++;

        if (sPtr >= s.size())
            return true;
    }

    return false;
}

int main(int argc, char const *argv[])
{
    if (argc != 3) {
        cout << "subsequence <s> <t>" << endl;
        return 1;
    }
    cout << isSubsequence(argv[1], argv[2]) << endl;
    return 0;
}
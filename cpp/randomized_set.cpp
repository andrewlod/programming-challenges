#include <iostream>
#include <vector>
#include <random>
#include <unordered_map>
#include "util/util.hpp"

using namespace std;
using namespace andrewlod::util;

/**
 * A Randomized Set must be able to insert and delete on O(1) time complexity and get uniformly random elements.
 */
class RandomizedSet {
private:
        mt19937 gen;
        unordered_map<int, int> idxs;
        vector<int> values;
public:
    RandomizedSet() {
        random_device rd;
        this->gen = mt19937(rd());
    }
    
    bool insert(int val) {
        if (this->idxs.count(val))
            return false;

        this->values.push_back(val);
        this->idxs[val] = this->values.size()-1;
        return true;
    }
    
    bool remove(int val) {
        if (!this->idxs.count(val))
            return false;

        int idx = this->idxs[val];
        this->values[idx] = this->values[this->values.size()-1];
        this->values.pop_back();

        this->idxs.erase(val);
        if (this->values.size() > 0)
            this->idxs[this->values[idx]] = idx;
            
        return true;
    }
    
    int getRandom() {
        std::uniform_int_distribution<> distrib(0, this->values.size()-1);
        return this->values[distrib(gen)];
    }
};

int main(int argc, char const *argv[])
{
    RandomizedSet rs;
    rs.insert(0);
    rs.remove(0);
    rs.insert(1);
    rs.insert(223);
    rs.insert(27381);
    cout << rs.getRandom() << endl;
    
    return 0;
}

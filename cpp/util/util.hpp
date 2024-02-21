#include <vector>
#include <string>
#include <iostream>

namespace andrewlod {
    namespace util {
        std::vector<std::string> split(const std::string& str, char delimiter = ',');
        std::vector<int> splitToInt(const std::string& str, char delimiter = ',');

        template<typename T>
        void printVector(const std::vector<T>& vec) {
            std::cout << "[";
            for (int i = 0; i < vec.size() - 1; i++) {
                std::cout << vec[i] << ", ";
            }
            std::cout << vec[vec.size()-1] << "]" << std::endl;
        }
    }
}
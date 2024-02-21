#include "util.hpp"

namespace andrewlod {
    namespace util {
        std::vector<std::string> split(const std::string& str, char delimiter) {
            std::vector<std::string> parts;

            size_t start = 0;
            size_t end;
            while ((end = str.find(delimiter, start)) != str.npos) {
                parts.push_back(str.substr(start, end-start));
                start = end + 1;
            }

            parts.push_back(str.substr(start, str.size()-1));
            return parts;
        }

        std::vector<int> splitToInt(const std::string& str, char delimiter) {
            std::vector<int> parts;

            size_t start = 0;
            size_t end;
            while ((end = str.find(delimiter, start)) != str.npos) {
                parts.push_back(std::stoi(str.substr(start, end-start)));
                start = end + 1;
            }

            parts.push_back(std::stoi(str.substr(start, str.size()-1)));
            return parts;
        }
    }
}
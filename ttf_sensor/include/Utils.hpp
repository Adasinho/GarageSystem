#ifndef UTILS_HPP
#define UTILS_HPP

#include "nlohmann/json.hpp"

using json = nlohmann::json;

namespace Utils {
    json getJsonData(std::string);
}

#endif // UTILS_HPP
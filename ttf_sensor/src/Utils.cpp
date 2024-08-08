#include "Utils.hpp"

#include <fstream>

json Utils::getJsonData(std::string filePath)
{
    std::ifstream file(filePath);
    json data = json::parse(file);

    return data;
}
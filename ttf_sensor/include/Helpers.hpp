#ifndef HELPERS_HPP
#define HELPERS_HPP

#include "ttf_sensor_api.pb.h"

#include "TTFSensorModel.hpp"

using ttf_sensor_api::TTFSensorId;

namespace Helpers {
    TTFSensorId getTTFSensorIDFromName(std::string name);
    std::string getTTFSensorIDName(TTFSensorId id);
    bool isCorrectTTFSensorId(TTFSensorId id);
    TTFSensorModel getTTFSensorModelFromString(std::string model);
}

#endif // HELPERS_HPP
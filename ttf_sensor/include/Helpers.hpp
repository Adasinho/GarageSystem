#include "ttf_sensor_api.pb.h"

using ttf_sensor_api::TTFSensorId;

namespace Helpers {
    TTFSensorId getTTFSensorIDFromName(std::string name);
    std::string getTTFSensorIDName(TTFSensorId id);
    bool isCorrectTTFSensorId(TTFSensorId id);
}
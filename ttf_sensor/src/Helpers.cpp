#include "Helpers.hpp"

using ttf_sensor_api::TTFSensorId;

TTFSensorId Helpers::getTTFSensorIDFromName(std::string name)
{
    if(name == "gate_a_parking_ttf_sensor") return TTFSensorId::GATE_A_PARKING_TTF_SENSOR_ID;
    else if(name == "gate_a_position_ttf_sensor") return TTFSensorId::GATE_A_POSITION_TTF_SENSOR_ID;
    else if(name == "gate_b_parking_ttf_sensor") return TTFSensorId::GATE_B_PARKING_TTF_SENSOR_ID;
    else if(name == "gate_b_position_ttf_sensor") return TTFSensorId::GATE_B_POSITION_TTF_SENSOR_ID;
    else return TTFSensorId::UNKNOWN_TTF_SENSOR_ID;
}

std::string Helpers::getTTFSensorIDName(TTFSensorId id)
{
    switch(id) {
        case TTFSensorId::GATE_A_PARKING_TTF_SENSOR_ID:
            return "GATE A PARKING";
        case TTFSensorId::GATE_A_POSITION_TTF_SENSOR_ID:
            return "GATE A POSITION";
        case TTFSensorId::GATE_B_PARKING_TTF_SENSOR_ID:
            return "GATE B PARKING";
        case TTFSensorId::GATE_B_POSITION_TTF_SENSOR_ID:
            return "GATE B POSITION";
        default:
            return "UNSUPPORTED SENSOR";
    }
}

bool Helpers::isCorrectTTFSensorId(TTFSensorId id)
{
    switch(id)
    {
        case TTFSensorId::GATE_A_PARKING_TTF_SENSOR_ID:
        case TTFSensorId::GATE_A_POSITION_TTF_SENSOR_ID:
        case TTFSensorId::GATE_B_PARKING_TTF_SENSOR_ID:
        case TTFSensorId::GATE_B_POSITION_TTF_SENSOR_ID:
            return true;
        default:
            return false;
    }
}

TTFSensorModel Helpers::getTTFSensorModelFromString(std::string model)
{
    if(model == "vl53l1x") return TTFSensorModel::TTF_SENSOR_MODEL_VL53L1X;
    else return TTFSensorModel::TTF_SENSOR_MODEL_UNKNOWN;
}
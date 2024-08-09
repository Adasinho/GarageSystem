#include "TTFSensorServicer.hpp"

Status TTFSensorServicer::GetMeasure(ServerContext *context, const MeasureRequest *request, MeasureResponse *reply)
{
    TTFSensorId id = request->id();
    std::cout << "Otrzymano żądanie pomiaru dla czujnika: " << id << std::endl;

    // Tutaj umieść logikę odczytu stanu czujnika
    int32_t distance = 123;  // Przykładowy stan czujnika

    reply->set_distance(distance);
    return Status::OK;
}
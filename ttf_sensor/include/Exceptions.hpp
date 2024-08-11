#include <exception>
#include <string>

class TTFSensorException : public std::exception
{
    public:
    TTFSensorException(const std::string& message) : message_(message) {}

    const char* what() const noexcept override
    {
        return message_.c_str();
    }

    protected:
    std::string message_;
};

class TTFSensorInicializationException : public TTFSensorException
{
    public:
    TTFSensorInicializationException(const std::string& message) : TTFSensorException(message) {}
};

class TTFSensorConfigurationException : public TTFSensorException
{
    public:
    TTFSensorConfigurationException(const std::string& message) : TTFSensorException(message) {}
};
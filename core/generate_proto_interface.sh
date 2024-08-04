GENERATE_PATH="./grpc_src"

python -m venv venv
source ./venv/bin/activate

# Generate Python files
python3 -m grpc_tools.protoc -I=./../digital_sensor/proto --python_out=grpc_src --grpc_python_out=grpc_src --pyi_out=grpc_src ./../digital_sensor/proto/digital_sensor_api.proto
python3 -m grpc_tools.protoc -I=./../ttf_sensor/proto --python_out=grpc_src --grpc_python_out=grpc_src --pyi_out=grpc_src ./../ttf_sensor/proto/ttf_sensor_api.proto

export PYTHONPATH=$PYTHONPATH:$(pwd)/grpc_src
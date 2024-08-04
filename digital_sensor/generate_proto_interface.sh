GENERATE_PATH="./grpc_src"

python -m venv venv
source ./venv/bin/activate

# Generate Python files
python3 -m grpc_tools.protoc -I=proto --python_out=grpc_src --grpc_python_out=grpc_src --pyi_out=grpc_src proto/digital_sensor_api.proto

export PYTHONPATH=$PYTHONPATH:$(pwd)/grpc_src
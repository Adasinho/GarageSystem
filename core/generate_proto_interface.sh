GENERATE_PATH="./grpc_src"

python -m venv venv
source ./venv/bin/activate

# Generate Python files
python3 -m grpc_tools.protoc -I=../protos --python_out=grpc_src --grpc_python_out=grpc_src --pyi_out=grpc_src ../protos/digital_sensor_api.proto
python3 -m grpc_tools.protoc -I=../protos --python_out=grpc_src --grpc_python_out=grpc_src --pyi_out=grpc_src ../protos/ttf_sensor_api.proto

export PYTHONPATH=$PYTHONPATH:$(pwd)/grpc_src
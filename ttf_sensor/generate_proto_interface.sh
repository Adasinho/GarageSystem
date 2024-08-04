GENERATE_PATH="./grpc_src"

export PATH=$PATH:/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/tools/grpc/

# Generate C++ files
#protoc -I proto/ --cpp_out=grpc_src --grpc_out=grpc_src --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` proto/ttf_sensor_api.proto
PROTOC_PATH="/home/adasinho/Adasinho/vcpkg/installed/arm64-linux/tools/protobuf/"
PROTOC_BIN_PATH=$PROTOC_PATH/protoc
GRPC_PATH="/home/adasinho/Adasinho/vcpkg/installed/arm64-linux/tools/grpc/"
GRPC_CPP_PLUGIN_PATH=$GRPC_PATH/grpc_cpp_plugin

$PROTOC_BIN_PATH -I proto/ --cpp_out=grpc_src --grpc_out=grpc_src --plugin=protoc-gen-grpc=$GRPC_CPP_PLUGIN_PATH proto/ttf_sensor_api.proto
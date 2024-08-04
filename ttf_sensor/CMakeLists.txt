cmake_minimum_required(VERSION 3.10)

project(ttf_sensor_server)

include(/home/adasinho/Adasinho/vcpkg/scripts/buildsystems/vcpkg.cmake)
set(CMAKE_TOOLCHAIN_FILE "/home/adasinho/Adasinho/vcpkg/scripts/buildsystems/vcpkg.cmake")
set(CMAKE_PREFIX_PATH "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/share/grpc/")


#include("/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/share/grpc/gRPCConfig.cmake")
#set(openssl_DIR "/home/adasinho/Adasinho/vcpkg/packages/openssl_arm64-linux/share/openssl/")
#set(re2_DIR "/home/adasinho/Adasinho/vcpkg/packages/re2_arm64-linux/share/re2/")
#set(gRPC_DIR "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/share/grpc/")
#set(Protobuf_DIR "/home/adasinho/Adasinho/vcpkg/packages/protobuf_arm64-linux/share/protobuf/")
#set(upb_DIR "/home/adasinho/Adasinho/vcpkg/packages/upb_arm64-linux/share/upb/")
#set(utf8_range_DIR "/home/adasinho/Adasinho/vcpkg/packages/utf8-range_arm64-linux/share/utf8_range/")
#set(absl_DIR "/home/adasinho/Adasinho/vcpkg/packages/abseil_arm64-linux/share/absl/")

# Znajdź lokalną instalację gRPC
find_package(gRPC CONFIG REQUIRED)

if(gRPC_FOUND)
    message("gRPC FOUNDED")

    set(gRPC_DIR "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/share/grpc/")
    set(gRPC_INCLUDE_DIRS "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/include/")
    set(gRPC_LIBRARIES "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/lib/")

    # Ustaw ścieżki do plików nagłówkowych i bibliotek gRPC
    include_directories(${gRPC_INCLUDE_DIRS})

    message(STATUS "gRPC_INCLUDE_DIRS: " ${gRPC_INCLUDE_DIRS})
    message(STATUS "gRPC_LIBRARIES: " ${gRPC_LIBRARIES})

    list(APPEND CMAKE_LIBRARY_PATH ${gRPC_LIBRARIES})
endif()

find_package(absl REQUIRED)

if(absl_FOUND)
    message("absl FOUNDED")

    set(absl_DIR "/home/adasinho/Adasinho/vcpkg/packages/abseil_arm64-linux/share/absl/")
    set(absl_INCLUDE_DIRS "/home/adasinho/Adasinho/vcpkg/packages/abseil_arm64-linux/include/")
    set(absl_LIBRARIES "/home/adasinho/Adasinho/vcpkg/packages/abseil_arm64-linux/lib/")

    # Ustaw ścieżki do plików nagłówkowych i bibliotek ABSL
    include_directories(${absl_INCLUDE_DIRS})

    message(STATUS "absl_INCLUDE_DIRS: ${absl_INCLUDE_DIRS}")
    message(STATUS "absl_LIBRARIES: ${absl_LIBRARIES}")

    list(APPEND CMAKE_LIBRARY_PATH ${absl_LIBRARIES})
endif()

find_package(Protobuf REQUIRED)
if(Protobuf_FOUND)
    message("Protobuf FOUNDED")

    set(Protobuf_DIR "/home/adasinho/Adasinho/vcpkg/packages/protobuf_arm64-linux/share/protobuf/")
    set(Protobuf_INCLUDE_DIRS "/home/adasinho/Adasinho/vcpkg/packages/protobuf_arm64-linux/include/")
    set(Protobuf_LIBRARIES "/home/adasinho/Adasinho/vcpkg/packages/protobuf_arm64-linux/lib/")

    include_directories(${Protobuf_INCLUDE_DIRS})

    message(STATUS "Protobuf_INCLUDE_DIRS: ${Protobuf_INCLUDE_DIRS}")
    message(STATUS "Protobuf_LIBRARIES: ${Protobuf_LIBRARIES}")

    list(APPEND CMAKE_LIBRARY_PATH ${Protobuf_LIBRARIES})
endif()

# ustaw ścieżkę do wygenerowanych plików
message("SOURCE DIR: ${CMAKE_SOURCE_DIR}")
#include_directories("${CMAKE_SOURCE_DIR}/grpc_src")

# Dodaj plik źródłowy serwera
#add_executable(ttf_sensor_server main.cpp)

# Dodaj ścieżki do bibliotek gRPC do zmiennej środowiskowej LD_LIBRARY_PATH (Linux/macOS)
# lub PATH (Windows) podczas uruchamiania
if(UNIX)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath,${gRPC_LIBRARY_DIRS}")
endif()

# Dodaj wygenerowane pliki .pb.cc i .grpc.pb.cc do projektu
file(GLOB_RECURSE PROTO_SOURCES "grpc_src/*.pb.cc" "grpc_src/*.grpc.pb.cc")
add_executable(ttf_sensor_server main.cpp ${PROTO_SOURCES})

# Ustaw ścieżki do bibliotek
### file(GLOB GRPC_LIBS "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/lib/*.a")
### file(GLOB ABSL_LIBS "/home/adasinho/Adasinho/vcpkg/packages/abseil_arm64-linux/lib/*.a")

# Połącz z bibliotekami gRPC
target_link_libraries(ttf_sensor_server PRIVATE gRPC::grpc++)
#target_link_libraries(ttf_sensor_server /home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/lib/)

message(STATUS "CMAKE_CXX_FLAGS: ${CMAKE_CXX_FLAGS}")




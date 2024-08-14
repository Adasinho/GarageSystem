cmake_minimum_required(VERSION 3.10)

project(ttf_sensor_server)

include(/home/adasinho/Adasinho/vcpkg/scripts/buildsystems/vcpkg.cmake)
set(CMAKE_TOOLCHAIN_FILE "/home/adasinho/Adasinho/vcpkg/scripts/buildsystems/vcpkg.cmake")
set(CMAKE_PREFIX_PATH "/home/adasinho/Adasinho/vcpkg/packages/grpc_arm64-linux/share/grpc/")

# Znajdź lokalną instalację gRPC oraz jego zależne biblioteki
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

# Inne zależności
find_package(nlohmann_json CONFIG REQUIRED)
if(nlohmann_json_FOUND)
    message(nlohmann_json FOUNDED)

    set(nlohmann_json_DIR "/home/adasinho/Adasinho/vcpkg/packages/nlohmann-json_arm64-linux/share/nlohmann_json/")
    set(nlohmann_json_INCLUDE_DIRS "/home/adasinho/Adasinho/vcpkg/packages/nlohmann-json_arm64-linux/include/")

    include_directories(${nlohmann_json_INCLUDE_DIRS})

    message(STATUS "nlohmann_json_INCLUDE_DIRS: ${nlohmann_json_INCLUDE_DIRS}")
endif()

# Dodaj pliki źródłowe .hpp do projektu
include_directories(${CMAKE_SOURCE_DIR}/include)
include_directories(${CMAKE_SOURCE_DIR}/include/interfaces)

# Zbierz pliki źródłowe .cpp
file(GLOB_RECURSE SOURCES "src/*.cpp")

# Dodaj wygenerowane pliki GRPC .pb.h oraz .grpc.pb.h do projektu
include_directories(${CMAKE_SOURCE_DIR}/grpc_src)

# Zbierz wygenerowane pliki .pb.cc i .grpc.pb.cc
file(GLOB_RECURSE PROTO_SOURCES "grpc_src/*.pb.cc" "grpc_src/*.grpc.pb.cc")

# Utwórz plik wykonywalny
add_executable(ttf_sensor_server main.cpp ${PROTO_SOURCES} ${SOURCES})


# Dodaj ścieżki do bibliotek gRPC do zmiennej środowiskowej LD_LIBRARY_PATH (Linux/macOS)
# lub PATH (Windows) podczas uruchamiania
if(UNIX)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath,${gRPC_LIBRARY_DIRS}")
endif()

# Połącz z bibliotekami gRPC
target_link_libraries(ttf_sensor_server PRIVATE gRPC::grpc++)




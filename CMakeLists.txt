cmake_minimum_required(VERSION 3.15)
project(sign_module)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(pybind11 REQUIRED)

add_library(sign_module MODULE src/bindings.cpp)

target_link_libraries(sign_module PRIVATE pybind11::module)

target_include_directories(sign_module PRIVATE ${pybind11_INCLUDE_DIRS})

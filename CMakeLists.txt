cmake_minimum_required(VERSION 3.18)
project(pypy LANGUAGES C)

find_package(Python REQUIRED Development)

set(CPYTHON_DIR "Testing" CACHE STRING "")
message(STATUS "CPython dir: ${CPYTHON_DIR}")

add_executable(generate cases_generator/generated_cases.c)
target_link_libraries(generate PRIVATE Python::Python)
target_include_directories(generate PRIVATE ${Python_INCLUDE_DIRS} "${CPYTHON_DIR}/Include/internal")
message(STATUS "${Python_INCLUDE_DIRS}")
message(STATUS "${CPYTHON_DIR}/Include/internal")
#add_definitions(-DPy_BUILD_CORE -DPyDict_MAXFREELIST)
add_definitions(-DPy_BUILD_CORE)

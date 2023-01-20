cmake_minimum_required(VERSION 3.0)
project(sample)

add_executable(sample_test tests/sample_test.cpp)

enable_testing()
add_test(NAME sample_test COMMAND $<TARGET_FILE:sample_test>)

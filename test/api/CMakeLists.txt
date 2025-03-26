# Create test executable
add_executable(api_test test_suite_1.cpp test_suite_2.cpp)

# Link test executable to dependent libraries
target_link_libraries(api_test
    PRIVATE
        GTest::gtest_main
        ProjectOptions
        api
)

# Enable test discovery
gtest_discover_tests(api_test)
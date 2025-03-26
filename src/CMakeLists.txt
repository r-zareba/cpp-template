add_subdirectory(api)
add_subdirectory(model)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} PRIVATE api)
target_include_directories(${PROJECT_NAME} PRIVATE api)

set(MODULE_NAME "api")

# Create module library
add_library(${MODULE_NAME} api.cpp)

# Add include directories for building and installing anagram
target_include_directories(${MODULE_NAME} PUBLIC  
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# add project options
target_link_libraries(${MODULE_NAME} PRIVATE ProjectOptions)

# Include module for GNU standard installation directories
include(GNUInstallDirs)

# Install library and executable and export as a set
install(TARGETS
${MODULE_NAME}
    EXPORT ${MODULE_NAME}ExportSet
)

# Install the export set
install(EXPORT ${MODULE_NAME}ExportSet
    FILE AnagramTargets.cmake
    NAMESPACE ${MODULE_NAME}::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${MODULE_NAME}
)
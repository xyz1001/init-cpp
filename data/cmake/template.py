"""
CMake 所需的相关文件mustache模板
"""

PROJECT_CMAKELISTS_TXT = """\
######################################################################
# Automatically generated by cppiniter ({{{version}}}) {{{date_time}}}
######################################################################

cmake_minimum_required (VERSION 3.0)
project ({{{project_name}}})

# include header
include_directories(${PROJECT_SOURCE_DIR}/dev/include)
include_directories(${PROJECT_SOURCE_DIR}/src)
include_directories(${PROJECT_SOURCE_DIR}/tests)

# CMake option
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug")
endif()
message(STATUS "Using default build type: " ${CMAKE_BUILD_TYPE})

if(CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)
    set(CMAKE_VS_INCLUDE_INSTALL_TO_DEFAULT_BUILD TRUE)
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU")
    set(CMAKE_CXX_FLAGS "$ENV{CXXFLAGS} ${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror")
    set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} ${CMAKE_CXX_FLAGS_DEBUG} -O0 -Wall -g2 -ggdb -D_GLIBCXX_DEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
endif()

# sub dir
add_subdirectory (src)
{{#is_lib}}
add_subdirectory (test)
{{/is_lib}}
"""

SRC_CMAKELISTS_TXT = """\
######################################################################
# Automatically generated by cppiniter ({{{version}}}) {{{date_time}}}
######################################################################

# source files
aux_source_directory(. SRC)

# target
{{#is_lib}}
add_library({{{project_name}}} SHARED ${SRC})
{{/is_lib}}
{{^is_lib}}
add_executable ({{{project_name}}} ${SRC})
{{/is_lib}}

# install
INSTALL(TARGETS {{{project_name}}}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
"""

TEST_CMAKELISTS_TXT = """\
######################################################################
# Automatically generated by cppiniter ({{{version}}}) {{{date_time}}}
######################################################################

# source files
aux_source_directory(. SRC)

# target
add_executable (catch ${SRC})

# link
target_link_libraries(catch {{{project_name}}})

# install
INSTALL(TARGETS catch
    RUNTIME DESTINATION bin)
"""

README_MD = """\
# {{{project_name}}}
"""

#####################################################################

FILES = {
    "PROJECT_CMAKELISTS_TXT": PROJECT_CMAKELISTS_TXT,
    "SRC_CMAKELISTS_TXT": SRC_CMAKELISTS_TXT,
    "TEST_CMAKELISTS_TXT": TEST_CMAKELISTS_TXT,
    "README_MD": README_MD
}

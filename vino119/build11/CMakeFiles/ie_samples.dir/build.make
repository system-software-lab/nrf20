# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/build11

# Utility rule file for ie_samples.

# Include the progress variables for this target.
include CMakeFiles/ie_samples.dir/progress.make

ie_samples: CMakeFiles/ie_samples.dir/build.make

.PHONY : ie_samples

# Rule to build all files generated by this target.
CMakeFiles/ie_samples.dir/build: ie_samples

.PHONY : CMakeFiles/ie_samples.dir/build

CMakeFiles/ie_samples.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ie_samples.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ie_samples.dir/clean

CMakeFiles/ie_samples.dir/depend:
	cd /home/pi/build11 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist /home/pi/build11 /home/pi/build11 /home/pi/build11/CMakeFiles/ie_samples.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ie_samples.dir/depend


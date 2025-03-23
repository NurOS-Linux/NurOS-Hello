# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Release")
  file(REMOVE_RECURSE
  "CMakeFiles/NurOS-Hello_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/NurOS-Hello_autogen.dir/ParseCache.txt"
  "NurOS-Hello_autogen"
  )
endif()

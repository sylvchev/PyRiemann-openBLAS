#----------------------------------------------------------------
# Generated CMake target import file for configuration "".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "armadillo" for configuration ""
set_property(TARGET armadillo APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(armadillo PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NOCONFIG "/opt/intel/composer_xe_2015.3.187/mkl/lib/intel64/libmkl_rt.so;/usr/lib/x86_64-linux-gnu/libsuperlu.so"
  IMPORTED_LOCATION_NOCONFIG "/usr/local/lib/libarmadillo.so.5.600.2"
  IMPORTED_SONAME_NOCONFIG "libarmadillo.so.5"
  )

list(APPEND _IMPORT_CHECK_TARGETS armadillo )
list(APPEND _IMPORT_CHECK_FILES_FOR_armadillo "/usr/local/lib/libarmadillo.so.5.600.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)

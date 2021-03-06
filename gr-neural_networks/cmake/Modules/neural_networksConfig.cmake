INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_NEURAL_NETWORKS neural_networks)

FIND_PATH(
    NEURAL_NETWORKS_INCLUDE_DIRS
    NAMES neural_networks/api.h
    HINTS $ENV{NEURAL_NETWORKS_DIR}/include
        ${PC_NEURAL_NETWORKS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    NEURAL_NETWORKS_LIBRARIES
    NAMES gnuradio-neural_networks
    HINTS $ENV{NEURAL_NETWORKS_DIR}/lib
        ${PC_NEURAL_NETWORKS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(NEURAL_NETWORKS DEFAULT_MSG NEURAL_NETWORKS_LIBRARIES NEURAL_NETWORKS_INCLUDE_DIRS)
MARK_AS_ADVANCED(NEURAL_NETWORKS_LIBRARIES NEURAL_NETWORKS_INCLUDE_DIRS)


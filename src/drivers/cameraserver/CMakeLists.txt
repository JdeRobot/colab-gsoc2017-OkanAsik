
SET( SOURCE_FILES cameraserver.cpp)

add_definitions(-DGLADE_DIR="${gladedir}")

include_directories(
	${INTERFACES_CPP_DIR}
	${LIBS_DIR}
	${CMAKE_CURRENT_SOURCE_DIR}
    	${easyiceconfig_INCLUDE_DIRS}
)

link_directories(
	${easyiceconfig_LIBRARY_DIRS}
)

add_executable (cameraserver ${SOURCE_FILES})

TARGET_LINK_LIBRARIES(cameraserver
    	jderobotutil
	${OpenCV_LIBRARIES}       
    	${OpenCVGUI_LIBRARIES} 
	colorspacesmm
	JderobotInterfaces
	${easyiceconfig_LIBRARIES} 
	${ZeroCIce_LIBRARIES}
	${CMAKE_THREAD_LIBS_INIT} 
	${ZLIB_LIBRARIES}
	logger
    	crypto
	ns
	${GLOG_LIBRARIES}
	)

install(TARGETS cameraserver
    DESTINATION ${CMAKE_INSTALL_PREFIX}/bin/
    COMPONENT drivers
    )
    
INSTALL (FILES ${CMAKE_CURRENT_SOURCE_DIR}/cameraserver.cfg DESTINATION ${CMAKE_INSTALL_PREFIX}/share/jderobot/conf)

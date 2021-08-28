cmake_minimum_required(VERSION 3.10)

project(cpp_program)

file(GLOB leetcode_SRC
     "*.cpp"
)

foreach(file_name ${leetcode_SRC})
	string( REPLACE ".cpp" "" base_file_name ${file_name} )

	get_filename_component(new_file_name ${base_file_name} NAME)

	message(${file_name})
	message(${new_file_name})
	
	add_executable(${new_file_name} ${file_name})
endforeach()

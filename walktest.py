import os


for in_path, in_subdirs, in_files in os.walk('.'):

    #print in_path
    #print in_subdirs
    #print in_files
    for in_filename in in_files:
        in_filepath = os.path.join(in_path, in_filename)

        print in_filepath



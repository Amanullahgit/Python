## script to rename all files in a directory from a list of file names

import os

# list of new filenames
new_filenames = ['new_file1.txt', 'new_file2.txt', 'new_file3.txt']

# directory containing the files to be renamed
directory = 'path/to/directory'

# get a list of all files in the directory
files = os.listdir(directory)

# rename each file
for i, file in enumerate(files):
    os.rename(os.path.join(directory, file), os.path.join(directory, new_filenames[i]))

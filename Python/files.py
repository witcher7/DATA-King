# os and pathlib are two modules in Python that provide functions for working with files and directories.
from os import path
print(path.abspath('.'))
# /users/gulat/OneDrive/Desktop/data-engineering/DATA-King/Python

print(type(path))
# <class 'module'>

from pathlib import Path
print(Path('.').absolute())
# /users/gulat/OneDrive/Desktop/data-engineering/DATA-King/Python
print(type(Path))
# <class 'type'>
# the difference is that os is a module that provides functions for working with files and directories, 
#  while pathlib is a module that provides an object-oriented interface for working with files and directories. 
# Path is a class in the pathlib module that represents a file system path.

from pathlib import Path
file_path = Path('data.txt')
print([m for m in dir(file_path) if not m.startswith('_')])

# current working directory
print(Path.cwd())
# /users/gulat/OneDrive/Desktop/data-engineering/DATA-King/Python

print(Path('main.py').exists())
print(Path('/Users/Rishabh/Desktop').exists())
# true 
print(Path("others.py").exists())
# False 

print(Path('main.py').is_file()) 
# True )
print(Path('/Users/Rishabh/Desktop').is_dir())
# True)

## List of file in the current directory
for f in Path('.').iterdir():
    print(f)    

## 
import os 
directory_path = "my_directory"
if not os.path.exists(directory_path):
    os.makedirs(directory_path) 
    print("Directory created successfully.")
else:
    print("Directory already exists.")

file_path= os.path.join(directory_path, "my_file.txt") 
# this will create a file path like "my_directory/my_file.txt"

# Getting parent directory 
parent_directory = os.path.dirname(file_path)
print(parent_directory)

is_file = os.path.isfile(file_path)
is_dir = os.path.isdir(directory_path)

# List file in a directory
dir_file = os.listdir(directory_path)
print(dir_file)

# remove directory
#
if os.path.exists(directory_path):
        for file in dir_file:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path) 
        os.rmdir(directory_path)


# CREATE NEW FILE
from pathlib import Path
directory_path = Path('my_directory')
if not directory_path.exists():
    directory_path.mkdir()
    print("Directory created successfully.")
else: 
     print("Directory already exists.")

# Creating path to the file
file_path = directory_path / 'my_file.txt'

# Check if the file exists, if not create it
if not file_path.exists():
    file_path.touch()
    print("File created successfully.")
else:
    print("File already exists.")

# Getting parent directory
parent_directory = file_path.parent
print(parent_directory)

# List files in a directory
dir_files = list(directory_path.iterdir())
for file in dir_files:
    print(file)
    print("----")

# Remove directory and its contents
if directory_path.exists():
    for file in dir_files:
        if file.is_file():
            file.unlink() 
    directory_path.rmdir()
else:
    print("Directory does not exist.")

# Better to use pathlib for file handling in Python as it provides a more intuitive 
# and object-oriented approach to working with files and directories. It also offers better support for different operating systems and i
# s generally considered more modern and easier to use than the os module.

# More on pathlib 
# Join paths 
from pathlib import Path
base_path = Path('/users/gulat/OneDrive/Desktop/data-engineering/DATA-King/Python') / "newfile.txt"
print(base_path)

# create dir 
path = Path("my_new_directory")
path.mkdir(parents=True, exist_ok=True)

# Absolute path
print(path.absolute())

# File name 
print(path.name)


# Reading and writing to files
with open('example.txt') as file:
   print(file.read())
# this will read the content and readlines will read the content line by line and return a list of lines.

with open("example.txt") as file: 
    print(file.readlines()) 

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
# this will overwrite the existing data 

# after writing to the file, we can read it again to see the changes but close the file first and then open it again to read the content.
file.close()
file = open("example.txt")
print(file.read())

with open("example.txt", "a") as file:
  file.write("This line will be appended to the file.\n")
# this will append the new data to the existing data in the file.

path('example.txt').unlink()
# this will delete the file example.txt from the current directory.

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
    
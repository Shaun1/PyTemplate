import sys
import os
sys.path.insert(0, os.path.abspath('..'))

# --- Import public things to test.
import my_package

# --- Import private things to test.
import my_package.my_executable_module as my_executable_module
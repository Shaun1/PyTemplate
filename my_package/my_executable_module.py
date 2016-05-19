#!/usr/bin/env python

"""This module is designed to be executed.

Note the path to the python interpreter on the first line and the use of
"if __name__ == '__main__':".
"""

#import python_built_ins
#import third_party
#import local

def say_hello():
	return 'Hello Python'

# --- This section will execute when the script is run
if __name__ == '__main__':
	print say_hello()
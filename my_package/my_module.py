""" This is a simple template for an importable Python module.

Here we can define variables, functions, and/or classes that can be imported
into another python program for reuse.

Don't forget to add Docstrings to functions and classes.
"""

#import python_built_ins
#import third_party
#import local

_MY_CONSTANT = True # --- underscore internal objects

def _my_function():
	"""Do something interesting."""
	return _MY_CONSTANT


class MyClass(object):
	"""Encapsulate methods and attributes with a Class."""
	def __init__(self):
		self.my_attribute = _my_function()

	def my_method(self):
		"""Return an attribute."""
		return self.my_attribute


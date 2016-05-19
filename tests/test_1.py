import unittest
from .context import my_package, my_executable_module

class MyUnitTests(unittest.TestCase):
	"""Always test your software"""

	def setUp(self):
		"""Anything that needs to be done pre-testing"""
		self.my_instance = my_package.MyClass()

	def tearDown(self):
		"""Anything you need to run after tests complete"""
		pass

	def test_one(self):
		"""Test a small functional unit"""
		self.assertTrue(self.my_instance.my_method())

	def test_two(self):
		"""Test something else."""
		self.assertIsInstance(my_executable_module.say_hello(), basestring)


if __name__ == '__main__':
	unittest.main()
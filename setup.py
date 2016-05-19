from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

setup(
	name='my_project',
	# Please see http://semver.org/spec/v2.0.0.html for versioning rules
	version='0.0.1',
	description='Template for creating Python Packages',
	long_description=readme,
	author='Shaun Houlihan',
	author_email='shaun@hedlabs.com',
	url='https://github.com/shaun1/PyTemplate',
	license=license,
	packages=find_packages(exclude=('tests', 'docs'))
	test_suite='nose.collector',
	tests_require=['nose']
)
from .context import my_package

def test_foo():
	assert my_package.foo() == 'bar'

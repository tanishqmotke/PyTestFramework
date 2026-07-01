import pytest

@pytest.fixture(scope="function")
def before_setup():
    print("This is the before setup method")
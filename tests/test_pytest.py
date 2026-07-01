
import pytest

@pytest.fixture(scope="module")
def setup_method():
    print("This is the setup method")

def test_my_first_test(setup_method):
    print("this is my first test")

def test_my_second_test(setup_method):
    print("this is my second test")

@pytest.fixture(scope="function")
def beforeMethod():
    print("This is the before method")
    yield
    print("This is the end of before method")
    
@pytest.fixture(scope="function")
def after_method():
    return "True"
    

def test_testcase1(beforeMethod,after_method):
    print("This is the test case")
    assert after_method == "False"
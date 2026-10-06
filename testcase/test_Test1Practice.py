import pytest

@pytest.fixture(scope="function")
def _secondFixture():
    print("This is the second fixture")
    yield
    print("End of the second Fixture")

def test_testcase1(_preinitialSetup):
    print("This is test case 1")

def test_testcase2(_preinitialSetup):
    print("This is test case 2")

def test_testcase3(_preinitialSetup,_secondFixture):
    print("This is test case 3")
    print(_preinitialSetup)
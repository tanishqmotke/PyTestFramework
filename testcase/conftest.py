
import pytest


@pytest.fixture(scope="session")
def getUserCredentails(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    
@pytest.fixture
def browser_instance(playwright,request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
         browser = playwright.firefox.launch(headless=False)
         
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def _preinitialSetupPart2():
    print("This is the setup before each function module:session")
    return "This is the value returned from Fixture preInitialSetup"

@pytest.fixture(scope="module")
def _preinitialSetup():
    print("This is the setup before each function")
    return "This is the value returned from Fixture preInitialSetup"

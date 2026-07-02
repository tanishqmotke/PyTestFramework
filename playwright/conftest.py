
import pytest


@pytest.fixture(scope="session")
def getUserCredentails(request):
    return request.param
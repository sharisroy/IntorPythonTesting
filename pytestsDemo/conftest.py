import pytest


# fixtures are used as setup and tear down methods for test cases - conftest file to generalize
# fixture are make it available to all test case

# @pytest.fixture() # call for every method
@pytest.fixture(scope='class') # call for only class label
def setup():
    print("\n------------I will be executing first")
    yield  # using yield to run last
    print("\n------------I will executing last")
    # close browser, clear choice, report generate


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Haris", "Chandra", "Roy"]

# this method call everytime, depends on params list
@pytest.fixture(params=['chrome', 'Firefox', 'IE'])
def crossBrowser(request):
    return request.param

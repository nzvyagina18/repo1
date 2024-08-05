import pytest
from fixture.address_book_lib import AddressBook

fixture = None


@pytest.fixture
def a_b(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseURL")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = AddressBook(browser = browser, base_url = base_url, login = login, password = password)
    else:
        if not fixture.is_valid():
            fixture = AddressBook(browser = browser, base_url = base_url, login = login, password = password)
    fixture.session.ensure_login(login, password)
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action = 'store', default = 'firefox')
    parser.addoption("--baseURL", action='store', default="http://localhost/addressbook/")
    parser.addoption("--login", action='store')
    parser.addoption("--password", action='store')


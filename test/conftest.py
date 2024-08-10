import pytest
import json
import os.path
from fixture.address_book_lib import AddressBook

fixture = None
target = None

@pytest.fixture
def a_b(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = AddressBook(browser=browser, base_url=target['baseURL'], login=target['username'],password=target['password'])
    fixture.session.ensure_login(username=target["username"],password=target["password"])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox')
    parser.addoption("--target", action='store', default="target.json")
    #parser.addoption("--baseURL", action='store', default="http://localhost/addressbook/")
    #parser.addoption("--login", action='store')
    #parser.addoption("--password", action='store')


import pytest
from fixture.address_book_lib import AddressBook

fixture = None


@pytest.fixture
def a_b(request):
    global fixture
    if fixture is None:
        fixture = AddressBook()
        fixture.session.login("admin", "secret")
    else:
        if not fixture.is_valid():
            fixture = AddressBook()
            fixture.session.login("admin", "secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


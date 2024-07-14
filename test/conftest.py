import pytest
from fixture.address_book_lib import AddressBook

fixture = None


@pytest.fixture
def a_b(request):
    global fixture
    if fixture is None:
        fixture = AddressBook()
    else:
        if not fixture.is_valid():
            fixture = AddressBook()
    fixture.session.ensure_login("admin", "secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


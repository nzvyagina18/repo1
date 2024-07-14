import pytest
from fixture.address_book_lib import AddressBook


@pytest.fixture #(scope='session')
def a_b(request):
    fixture = AddressBook()
    fixture.session.login("admin", "secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

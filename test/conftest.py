import pytest
from fixture.address_book_lib import AddressBook


@pytest.fixture(scope='session')
def a_b(request):
    fixture = AddressBook()
    request.addfinalizer(fixture.destroy)
    return fixture

# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from contact_page import ContactPage
from contact_date import ContactDate
from address_book_lib import AddressBook

@pytest.fixture
def a_b(request):
    fixture = AddressBook()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(a_b):
    a_b.login("admin", "secret")
    a_b.add_contact(Contact("Contact1", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020") ), ContactPage())
    a_b.logout()
# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.address_book_lib import AddressBook


@pytest.fixture
def a_b(request):
    fixture = AddressBook()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(a_b):
    a_b.login( "admin", "secret")
    a_b.create_group(Group("aaa", "bbb", "ccc"))
    a_b.logout()


def test_create_empty_group(a_b):
    a_b.login("admin", "secret")
    a_b.create_group(Group("", "", ""))
    a_b.logout()

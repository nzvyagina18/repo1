# -*- coding: utf-8 -*-
from model.contact import Contact
from model.contact_page import ContactPage
from model.contact_date import ContactDate
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10# + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits # + string.punctuation + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname = random_string("first", 10), lastname = random_string("last", 10), homephone= random_phone(10))
            for i in range(5)
            ]
@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(a_b, new_contact):
    old_contacts = a_b.contact.get_contact_list()
    #new_contact = Contact(firstname = "test_add", lastname = "Contact1_last")
    a_b.contact.add(new_contact, ContactPage())
    new_contacts = a_b.contact.get_contact_list()
    assert len(old_contacts) == a_b.contact.count() - 1
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_firstname(a_b):
    contact_to_edit = 'test_edit'
    if not a_b.contact.exists(contact_to_edit):
        a_b.contact.add(Contact(firstname="test_edit"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    contact_data = Contact(firstname = contact_to_edit + '_updated')
    for el in old_contacts:
        if el.firstname == contact_to_edit:
            contact_data.id = el.id
            break
    a_b.contact.edit(contact_to_edit, contact_data, ContactPage())
    new_contacts = a_b.contact.get_contact_list()
    assert len(old_contacts) == a_b.contact.count()
    for el in old_contacts:
        if el.id == contact_data.id:
            el.firstname = contact_data.firstname
            break
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact(a_b):
    if not a_b.contact.exists_any():
        a_b.contact.add(Contact(firstname="test"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_data = Contact(firstname = 'test_updated')
    contact_data.id = old_contacts[index].id
    a_b.contact.edit_by_index(index, contact_data, ContactPage())
    new_contacts = a_b.contact.get_contact_list()

    assert len(old_contacts) == a_b.contact.count()
    for el in old_contacts:
        if el.id == contact_data.id:
            el.firstname = contact_data.firstname
            break
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_nick(a_b):
    if not a_b.contact.exists('test_edit_nick'):
        a_b.contact.add(Contact(firstname="test_edit_nick"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    a_b.contact.edit('test_edit_nick', Contact( nickname="test_nick1"), ContactPage())
    assert len(old_contacts) == a_b.contact.count()


def test_del_from_home(a_b):
    if not a_b.contact.exists('to_delete_from_home'):
        a_b.contact.add(Contact(firstname="to_delete_from_home"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    a_b.contact.delete_from_home('to_delete_from_home')
    new_contacts = a_b.contact.get_contact_list()
    assert len(old_contacts) == a_b.contact.count() + 1
    old_contacts = sorted(old_contacts, key=Contact.id_or_max)
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    old_contacts[len(old_contacts)-1:len(old_contacts)] = []
    assert old_contacts == new_contacts


def test_del_some_from_home(a_b):
    if not a_b.contact.exists_any():
        a_b.contact.add(Contact(firstname="to_delete_from_home"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    index = randrange(len(old_contacts))
    a_b.contact.delete_by_index_from_home(index)
    new_contacts = a_b.contact.get_contact_list()
    assert len(old_contacts) == a_b.contact.count() + 1
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts


def test_del_from_edit(a_b):
    if not a_b.contact.exists('to_delete_from_edit'):
        a_b.contact.add(Contact(firstname="to_delete_from_edit"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    a_b.contact.delete_from_edit('to_delete_from_edit')
    new_contacts = a_b.contact.get_contact_list()
    assert len(old_contacts) == a_b.contact.count() + 1
    old_contacts = sorted(old_contacts, key=Contact.id_or_max)
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    old_contacts[len(old_contacts) - 1:len(old_contacts)] = []
    assert old_contacts == new_contacts

def test_del_some_from_edit(a_b):
    if not a_b.contact.exists_any():
        a_b.contact.add(Contact(firstname="to_delete_from_edit"), ContactPage())
    old_contacts = a_b.contact.get_contact_list()
    index = randrange(len(old_contacts))
    a_b.contact.delete_by_index_from_edit(index)
    new_contacts = a_b.contact.get_contact_list()
    assert len(old_contacts) == a_b.contact.count() + 1
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts




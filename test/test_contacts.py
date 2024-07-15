# -*- coding: utf-8 -*-
from model.contact import Contact
from model.contact_page import ContactPage
from model.contact_date import ContactDate


def test_add_contact(a_b):
    if a_b.contact.exists('test_add'):
        a_b.contact.delete_from_home("test_add")
    a_b.contact.add(Contact("test_add", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020"), "C:\\Users\\nadya\\desktop\\snegir.png"), ContactPage())


def test_edit_contact(a_b):
    if not a_b.contact.exists('test_edit'):
        print('test_edit not found, created')
        a_b.contact.add(Contact(firstname="test_edit"), ContactPage())
    a_b.contact.edit('test_edit', Contact("test_edit", "Contact1_nick1", "Contact1_last1", "Contact1_mid1", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020"), "C:\\Users\\nadya\\desktop\\snegir.png"), ContactPage())

def test_edit_contact_nick(a_b):
    if not a_b.contact.exists('test_edit_nick'):
        a_b.contact.add(Contact(firstname="test_edit_nick"), ContactPage())
    a_b.contact.edit('test_edit_nick', Contact( nickname="test_nick1"), ContactPage())


def test_del_from_home(a_b):
    if not a_b.contact.exists('to_delete_from_home'):
        a_b.contact.add(Contact(firstname="to_delete_from_home"), ContactPage())
    a_b.contact.delete_from_home('to_delete_from_home')

def test_del_from_edit(a_b):
    if not a_b.contact.exists('to_delete_from_edit'):
        a_b.contact.add(Contact(firstname="to_delete_from_edit"), ContactPage())
    a_b.contact.delete_from_edit('to_delete_from_edit')




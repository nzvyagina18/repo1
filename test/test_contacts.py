# -*- coding: utf-8 -*-
from model.contact import Contact
from model.contact_page import ContactPage
from model.contact_date import ContactDate


def test_add_contact(a_b):
    if a_b.contact.exists('contact_06') > 0:
        a_b.contact.delete_from_home("contact_06")
    a_b.contact.add(Contact("contact_06", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020"), "C:\\Users\\nadya\\desktop\\snegir.png"), ContactPage())


def test_edit_contact(a_b):
    if a_b.contact.exists('contact_06') == 0:
        a_b.contact.add(Contact(firstname="contact_06", fax_="3333333"), ContactPage())
    a_b.contact.edit('contact_06', Contact("contact_06", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020"), "C:\\Users\\nadya\\desktop\\snegir.png"), ContactPage())

def test_edit_contact_nick(a_b):
    if a_b.contact.exists('Contact2') == 0:
        a_b.contact.add(Contact(firstname="Contact2", fax_="3333333"), ContactPage())
    a_b.contact.edit('Contact2', Contact( nickname="test_nick", fax_="3333333"), ContactPage())


def test_del_from_home(a_b):
    if a_b.contact.exists('contact_06') == 0:
        a_b.contact.add(Contact(firstname="contact_06", fax_="3333333"), ContactPage())
    a_b.contact.delete_from_home('contact_06')

def test_del_from_edit(a_b):
    if a_b.contact.exists('contact_06') == 0:
        a_b.contact.add(Contact(firstname="contact_06", fax_="3333333"), ContactPage())
    a_b.contact.delete_from_edit('contact_06')




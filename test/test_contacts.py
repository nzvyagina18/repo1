# -*- coding: utf-8 -*-
from model.contact import Contact
from model.contact_page import ContactPage
from model.contact_date import ContactDate


def test_add_contact(a_b):
    a_b.session.login("admin", "secret")
    a_b.contact.add(Contact("Contact1", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020"), "C:\\Users\\nadya\\desktop\\snegir.png"), ContactPage())
    a_b.session.logout()


def test_edit_contact(a_b):
    a_b.session.login("admin", "secret")
    a_b.contact.edit('contact_05', Contact("contact_05", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020"), "C:\\Users\\nadya\\desktop\\snegir.png"), ContactPage())
    a_b.session.logout()


def test_del_from_home(a_b):
    a_b.session.login("admin", "secret")
    a_b.contact.delete_from_home('Contact1')
    a_b.session.logout()


def test_del_from_edit(a_b):
    a_b.session.login("admin", "secret")
    a_b.contact.delete_from_edit('Contact1')
    a_b.session.logout()


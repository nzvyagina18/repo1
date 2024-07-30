import re
from random import randrange
def test_contact_info_on_home_page(a_b):
    contacts_from_home_page = a_b.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = a_b.contact.get_contact_list()[index]
    contact_from_edit_page = a_b.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == remove_extra_spaces(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(a_b):
    contact_from_view_page = a_b.contact.get_contact_info_from_view_page(2)
    contact_from_edit_page = a_b.contact.get_contact_info_from_edit_page(2)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone

def clear(s):
    return re.sub("() -", "", s)

def remove_extra_spaces(s):
    return re.sub("\s+", " ", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x:clear(x),
                         filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3]))))
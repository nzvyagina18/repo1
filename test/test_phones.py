
def test_phones_on_home_page(a_b):
    contact_from_home_page = a_b.contact.get_contact_list()[2]
    contact_from_edit_page = a_b.contact.get_contact_info_from_edit_page(2)
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone

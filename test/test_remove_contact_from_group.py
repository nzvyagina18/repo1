from model.contact import Contact
from model.contact_page import ContactPage
from model.group import Group
import random

def test_remove_from_group(a_b, orm):
    if len(orm.get_contact_list()) == 0:
        a_b.contact.add(Contact(firstname="to_delete_from_edit"), ContactPage())
    if len(orm.get_group_list()) == 0:
        a_b.group.create('container')
    contact_id = random.choice(orm.get_contact_list()).id
    group_id = random.choice(orm.get_group_list()).id
    if not orm.contact_exists_in_group(contact_id, group_id):
        a_b.contact.add_to_group(contact_id, group_id)
        #a_b.contact.remove_from_group(contact_id, group_id)
    old_list = orm.get_contact_group_list_for_contact(group_id)
    #a_b.contact.add_to_group(contact_id, group_id)
    a_b.contact.remove_from_group(contact_id, group_id)
    new_list = orm.get_contact_group_list_for_contact(group_id)
    old_list.remove((int(contact_id), int(group_id)))
    assert sorted(old_list) == sorted(new_list)
from pony.orm import *
from model.group import Group
from model.contact import Contact
import re


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column= 'address')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')

    class ORMContactGroup(db.Entity):
        _table_ = 'address_in_groups'
        id = PrimaryKey(int, column='id')
        group_id = Optional(int, column='group_id')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home(self, contact):
        return "\n".join(filter(lambda x: x != "",
                         map(lambda x: self.clear(x), [contact.home_phone, contact.mobile_phone, contact.work_phone])))

    def merge_emails_like_on_home(self, contact):
        return "\n".join(filter(lambda x: x != "", [contact.email1, contact.email2, contact.email3]))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, address=contact.address,
                           all_emails_from_home_page=self.merge_emails_like_on_home(contact),
                           all_phones_from_home_page=self.merge_phones_like_on_home(contact))
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))

    def convert_contact_group_to_list(self, contact_groups):
        l = list()
        for i in contact_groups:
            l.append((i.id,i.group_id))
        return l
    @db_session
    def get_contact_group_list_for_contact(self, group_id):
        return self.convert_contact_group_to_list(select(cg for cg in ORMFixture.ORMContactGroup if cg.group_id == group_id))

    @db_session
    def contact_exists_in_group(self, contact_id, group_id):
        if len(self.convert_contact_group_to_list(
            select(cg for cg in ORMFixture.ORMContactGroup if cg.group_id == group_id and cg.id == contact_id)))>0:
            return True
        else:
            return False




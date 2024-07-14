# -*- coding: utf-8 -*-
from model.contact_date import ContactDate
class ContactPage:
    def __init__(self):
        self.firstname = 'firstname'
        self.nickname = 'nickname'
        self.lastname = 'lastname'
        self.midname = 'middlename'
        self.title = 'title'
        self.company = 'company'
        self.address = 'address'
        self.homephone = 'home'
        self.mobilephone = 'mobile'
        self.workphone = 'work'
        self.fax_ = 'fax',
        self.email1 = 'email'
        self.email2 = 'email2'
        self.email3 = 'email3'
        self.homepage = 'homepage'
        self.birthdate = ContactDate("bday", "bmonth", "byear")
        self.ann_date = ContactDate("aday", "amonth", "ayear")




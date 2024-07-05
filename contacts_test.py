# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact
from contact_page import ContactPage
from contact_date import ContactDate

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\nadya\PycharmProjects\repo1\geckodriver.exe',
                                    options=options)
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.add_contact(wd, Contact("Contact1", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru", ContactDate("11", "June", "2000"), ContactDate("11", "June", "2020") ), ContactPage())
        self.logout(wd)

    def add_contact(self, wd, contact, contact_page):
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("add new").click()
        self.upload_photo(wd, "C:\\Users\\nadya\\desktop\\snegir.png")
        self.populate(wd, contact_page.firstname, contact.firstname)
        self.populate(wd, contact_page.midname, contact.midname)
        self.populate(wd, contact_page.lastname, contact.lastname)
        self.populate(wd, contact_page.nickname, contact.nickname)
        self.populate(wd, contact_page.title, contact.title)
        self.populate(wd, contact_page.company, contact.company)
        self.populate(wd, contact_page.address, contact.address)
        self.populate(wd, contact_page.homephone, contact.homephone)
        self.populate(wd, contact_page.mobilephone, contact.mobilephone)
        self.populate(wd, contact_page.workphone, contact.workphone)
        self.populate(wd, contact_page.fax, contact.fax)
        self.populate(wd, contact_page.email1, contact.email1)
        self.populate(wd, contact_page.email2, contact.email2)
        self.populate(wd, contact_page.email3, contact.email3)
        self.populate(wd, contact_page.homepage, contact.homepage)
        self.set_date(wd, contact_page.birthdate, contact.birthdate)
        self.set_date(wd, contact_page.ann_date, contact.ann_date)
        #submit form
        wd.find_element_by_name("submit").click()
        #self.upload_photo(wd, "C:\\Users\\nadya\\desktop\\snegir.png")

    def populate(self, wd, fieldname, value):
        wd.find_element_by_name(fieldname).click()
        wd.find_element_by_name(fieldname).clear()
        wd.find_element_by_name(fieldname).send_keys(value)

    def upload_photo(self, wd, path):
        wd.find_element_by_name("photo").send_keys(path)

    def set_date(self, wd, date_control, date_value):
        wd.find_element_by_name(date_control.day).click()
        Select(wd.find_element_by_name(date_control.day)).select_by_visible_text(date_value.day)
        wd.find_element_by_name(date_control.month).click()
        Select(wd.find_element_by_name(date_control.month)).select_by_visible_text(date_value.month)
        wd.find_element_by_name(date_control.year).click()
        wd.find_element_by_name(date_control.year).clear()
        wd.find_element_by_name(date_control.year).send_keys(date_value.year)


    #all the staff below + setUp method should be moved to address_book_lib.py but currently I do not know how)
    def login(self, wd, admin, secret):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(admin)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
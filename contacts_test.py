# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact
from contact_page import ContactPage

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\nadya\PycharmProjects\repo1\geckodriver.exe',
                                    options=options)
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd, "admin", "secret")
        self.add_contact(wd, Contact("Contact1", "Contact1_nick", "Contact1_last", "Contact1_mid", "Contact1_title",
                         "Contact1_company", "Contact1 address", "2222222", "+79212222222", "+79112222222", "2222222",
                         "contact1@email1.ru", "contact1@email2.ru", "contact1@email3.ru", "http://mail.ru"))
        self.Logout(wd)

    def add_contact(self, wd, Contact):
        page = ContactPage()
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("add new").click()
        self.populate(wd, page.firstname, Contact.firstname)
        self.populate(wd, page.midname, Contact.midname)
        self.populate(wd, page.lastname, Contact.lastname)
        self.populate(wd, page.nickname, Contact.nickname)
        self.populate(wd, page.title, Contact.title)
        self.populate(wd, page.company, Contact.company)
        self.populate(wd, page.address, Contact.address)
        self.populate(wd, page.homephone, Contact.homephone)
        self.populate(wd, page.mobilephone, Contact.mobilephone)
        self.populate(wd, page.workphone, Contact.workphone)
        self.populate(wd, page.fax, Contact.fax)
        self.populate(wd, page.email1, Contact.email1)
        self.populate(wd, page.email2, Contact.email2)
        self.populate(wd, page.email3, Contact.email3)
        self.populate(wd, page.homepage, Contact.homepage)
        self.set_birthdate(wd)
        self.set_anniversary(wd)
        #submit form
        wd.find_element_by_name("submit").click()
        #self.upload_photo(wd, "C:\\Users\\nadya\\desktop\\snegir.png")

    def populate(self, wd, fieldname, value):
        wd.find_element_by_name(fieldname).click()
        wd.find_element_by_name(fieldname).clear()
        wd.find_element_by_name(fieldname).send_keys(value)

    def upload_photo(self, wd, path):
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys(path)
        wd.find_element_by_name("submit").click()

    def set_anniversary(self, wd):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("11")
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("June")
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2030")

    def set_birthdate(self, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("11")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2000")

    #all the staff below + setUp method should be moved to address_book_lib but currently I do not know how)
    def Login(self, wd, admin, secret):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(admin)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def OpenHomePage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
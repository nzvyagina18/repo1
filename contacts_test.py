# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

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
        self.add_contact(wd)
        self.Logout(wd)

    def add_contact(self, wd, firstname="Contact1", midname="Contact1_mid", lastname="Contact1_last",
                    nickname="Contact1_nick", title="Contact1_title", company="Contact1_company",
                    address="Contact1 address", homephone="2222222", mobilephone="+79212222222", workphone="+79112222222",
                    fax="2222222", email1="contact1@email1.ru", email2="contact1@email2.ru", email3="contact1@email3.ru",
                    homepage="http://mail.ru"):
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("add new").click()
        self.populate(wd, 'firstname', firstname)
        self.populate(wd, 'middlename', midname)
        wd.find_element_by_name("theform").click()
        self.populate(wd, 'lastname', lastname)
        self.populate(wd, 'nickname', nickname)
        self.populate(wd, 'title', title)
        self.populate(wd, 'company', company)
        self.populate(wd, 'address', address)
        self.populate(wd, 'home', homephone)
        self.populate(wd, 'mobile', mobilephone)
        self.populate(wd, 'work', workphone)
        self.populate(wd, 'fax', fax)
        self.populate(wd, 'email', email1)
        self.populate(wd, 'email2', email2)
        self.populate(wd, 'email3', email3)
        self.populate(wd, 'homepage', homepage)
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
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[13]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[7]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2030")

    def set_birthdate(self, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("11")
        wd.find_element_by_xpath("//option[@value='11']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//option[@value='June']").click()
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
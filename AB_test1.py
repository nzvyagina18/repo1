# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\nadya\PycharmProjects\repo1\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)

    def test_create_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_group(wd, Group("aaa", "bbb", "ccc"))
        self.logout(wd)

    def test_create_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_group(wd, Group("", "", ""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
        # Open Groups page
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()
        # initiate group creation
        wd.find_element_by_name("new").click()
        # fill in group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit form
        wd.find_element_by_name("submit").click()
        # return to groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, user, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

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

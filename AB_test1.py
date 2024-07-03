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
        self.OpenHomePage(wd)
        self.Login(wd, "admin", "secret")
        self.OpenGroupsPage(wd)
        self.CreateGroup(wd, Group("aaa", "bbb", "ccc"))
        self.ReturnToGroupsPage(wd)
        self.Logout(wd)

    def test_create_empty_group(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd, "admin", "secret")
        self.OpenGroupsPage(wd)
        self.CreateGroup(wd, Group("", "", ""))
        self.ReturnToGroupsPage(wd)
        self.Logout(wd)

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def ReturnToGroupsPage(self, wd):
        wd.find_element_by_link_text("groups").click()

    def CreateGroup(self, wd, Group):
        # initiate group creation
        wd.find_element_by_name("new").click()
        # fill in group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        # submit form
        wd.find_element_by_name("submit").click()

    def OpenGroupsPage(self, wd):
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, user, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def OpenHomePage(self, wd):
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

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class AddressBook:
    def __init__(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\nadya\PycharmProjects\repo1\geckodriver.exe',
                                        options=options)
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, user, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, group):
        # Open Groups page
        wd = self.wd
        self.open_groups_page()
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
        self.return_to_groups_page()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()

    def is_alert_present(self):
            try:
                self.wd.switch_to_alert()
            except NoAlertPresentException as e:
                return False
            return True
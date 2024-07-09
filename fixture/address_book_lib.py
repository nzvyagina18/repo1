from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class AddressBook:
    def __init__(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'/geckodriver.exe',
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

    def populate(self, fieldname, value):
        wd = self.wd
        wd.find_element_by_name(fieldname).click()
        wd.find_element_by_name(fieldname).clear()
        wd.find_element_by_name(fieldname).send_keys(value)

    def upload_photo(self, path):
        wd = self.wd
        wd.find_element_by_name("photo").send_keys(path)

    def set_date(self, date_control, date_value):
        wd = self.wd
        wd.find_element_by_name(date_control.day).click()
        Select(wd.find_element_by_name(date_control.day)).select_by_visible_text(date_value.day)
        wd.find_element_by_name(date_control.month).click()
        Select(wd.find_element_by_name(date_control.month)).select_by_visible_text(date_value.month)
        wd.find_element_by_name(date_control.year).click()
        wd.find_element_by_name(date_control.year).clear()
        wd.find_element_by_name(date_control.year).send_keys(date_value.year)

    def add_contact(self, contact, contact_page):
        wd = self.wd
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("add new").click()
        self.upload_photo( "C:\\Users\\nadya\\desktop\\snegir.png")
        self.populate( contact_page.firstname, contact.firstname)
        self.populate( contact_page.midname, contact.midname)
        self.populate( contact_page.lastname, contact.lastname)
        self.populate( contact_page.nickname, contact.nickname)
        self.populate( contact_page.title, contact.title)
        self.populate( contact_page.company, contact.company)
        self.populate( contact_page.address, contact.address)
        self.populate( contact_page.homephone, contact.homephone)
        self.populate( contact_page.mobilephone, contact.mobilephone)
        self.populate( contact_page.workphone, contact.workphone)
        self.populate( contact_page.fax, contact.fax)
        self.populate( contact_page.email1, contact.email1)
        self.populate( contact_page.email2, contact.email2)
        self.populate( contact_page.email3, contact.email3)
        self.populate( contact_page.homepage, contact.homepage)
        self.set_date( contact_page.birthdate, contact.birthdate)
        self.set_date( contact_page.ann_date, contact.ann_date)
        #submit form
        wd.find_element_by_name("submit").click()

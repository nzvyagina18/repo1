from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class AddressBook:
    def __init__(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'geckodriver.exe',
                                    options=options)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


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

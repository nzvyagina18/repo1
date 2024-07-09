from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, ab):
        self.ab = ab

    def populate(self, fieldname, value):
        wd = self.ab.wd
        wd.find_element_by_name(fieldname).click()
        wd.find_element_by_name(fieldname).clear()
        wd.find_element_by_name(fieldname).send_keys(value)

    def upload_photo(self, path):
        wd = self.ab.wd
        wd.find_element_by_name("photo").send_keys(path)

    def set_date(self, date_control, date_value):
        wd = self.ab.wd
        wd.find_element_by_name(date_control.day).click()
        Select(wd.find_element_by_name(date_control.day)).select_by_visible_text(date_value.day)
        wd.find_element_by_name(date_control.month).click()
        Select(wd.find_element_by_name(date_control.month)).select_by_visible_text(date_value.month)
        wd.find_element_by_name(date_control.year).click()
        wd.find_element_by_name(date_control.year).clear()
        wd.find_element_by_name(date_control.year).send_keys(date_value.year)

    def add(self, contact, contact_page):
        wd = self.ab.wd
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("add new").click()
        self.upload_photo("C:\\Users\\nadya\\desktop\\snegir.png")
        self.populate(contact_page.firstname, contact.firstname)
        self.populate(contact_page.midname, contact.midname)
        self.populate(contact_page.lastname, contact.lastname)
        self.populate(contact_page.nickname, contact.nickname)
        self.populate(contact_page.title, contact.title)
        self.populate(contact_page.company, contact.company)
        self.populate(contact_page.address, contact.address)
        self.populate(contact_page.homephone, contact.homephone)
        self.populate(contact_page.mobilephone, contact.mobilephone)
        self.populate(contact_page.workphone, contact.workphone)
        self.populate(contact_page.fax, contact.fax)
        self.populate(contact_page.email1, contact.email1)
        self.populate(contact_page.email2, contact.email2)
        self.populate(contact_page.email3, contact.email3)
        self.populate(contact_page.homepage, contact.homepage)
        self.set_date(contact_page.birthdate, contact.birthdate)
        self.set_date(contact_page.ann_date, contact.ann_date)
        # submit form
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

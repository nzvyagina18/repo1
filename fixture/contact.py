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
        self.upload_photo(contact.photo) #"C:\\Users\\nadya\\desktop\\snegir.png"
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

    def edit(self, contact_name, contact_new, contact_page):
        wd = self.ab.wd
        checkbox = '//input [contains(@title,"' + contact_name + '")]'
        contact_id = wd.find_element_by_xpath(checkbox).get_attribute("id")
        edit_button = '//a[@href = "edit.php?id=' + contact_id + '"]/img'
        wd.find_element_by_xpath(edit_button).click()
        self.upload_photo(contact_new.photo)
        self.populate(contact_page.firstname, contact_new.firstname)
        self.populate(contact_page.midname, contact_new.midname)
        self.populate(contact_page.lastname, contact_new.lastname)
        self.populate(contact_page.nickname, contact_new.nickname)
        self.populate(contact_page.title, contact_new.title)
        self.populate(contact_page.company, contact_new.company)
        self.populate(contact_page.address, contact_new.address)
        self.populate(contact_page.homephone, contact_new.homephone)
        self.populate(contact_page.mobilephone, contact_new.mobilephone)
        self.populate(contact_page.workphone, contact_new.workphone)
        self.populate(contact_page.fax, contact_new.fax)
        self.populate(contact_page.email1, contact_new.email1)
        self.populate(contact_page.email2, contact_new.email2)
        self.populate(contact_page.email3, contact_new.email3)
        self.populate(contact_page.homepage, contact_new.homepage)
        self.set_date(contact_page.birthdate, contact_new.birthdate)
        self.set_date(contact_page.ann_date, contact_new.ann_date)
        # update form
        wd.find_element_by_name("update").click()

    def delete_from_edit(self, contact_name):
        wd = self.ab.wd
        checkbox = '//input [contains(@title,"' + contact_name + '")]'
        contact_id = wd.find_element_by_xpath(checkbox).get_attribute("id")
        edit_button = '//a[@href = "edit.php?id=' + contact_id + '"]/img'
        wd.find_element_by_xpath(edit_button).click()
        # delete contact
        wd.find_element_by_xpath('//input[@value = "Delete"]').click()

    def delete_from_home(self, contact_name):
        wd = self.ab.wd
        checkbox = '//input [contains(@title,"' + contact_name + '")]'
        wd.find_element_by_xpath(checkbox).click()
        wd.find_element_by_xpath('//input[@value = "Delete"]').click()



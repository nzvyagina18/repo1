from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, ab):
        self.ab = ab

    def open_contact_page(self):
        wd = self.ab.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def populate(self, fieldname, value):
        wd = self.ab.wd
        if value is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(value)

    def upload_photo(self, path):
        wd = self.ab.wd
        if path is not None:
            wd.find_element_by_name("photo").send_keys(path)

    def set_date(self, date_control, date_value):
        wd = self.ab.wd
        if date_value is not None:
            wd.find_element_by_name(date_control.day).click()
            Select(wd.find_element_by_name(date_control.day)).select_by_visible_text(date_value.day)
            wd.find_element_by_name(date_control.month).click()
            Select(wd.find_element_by_name(date_control.month)).select_by_visible_text(date_value.month)
            wd.find_element_by_name(date_control.year).click()
            wd.find_element_by_name(date_control.year).clear()
            wd.find_element_by_name(date_control.year).send_keys(date_value.year)

    def add(self, contact, contact_page):
        wd = self.ab.wd
        self.open_contact_page()
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("add new").click()
        self.populate_contact_data(contact, contact_page)
        self.submit_form()
        self.open_contact_page()

    def submit_form(self):
        # submit form
        wd = self.ab.wd
        wd.find_element_by_name("submit").click()

    def populate_contact_data(self, contact, contact_page):
        self.upload_photo(contact.photo)
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

    def edit(self, contact_name, contact_new, contact_page):
        wd = self.ab.wd
        self.open_contact_page()
        self.edit_contact(contact_name)
        self.populate_contact_data(contact_new, contact_page)
        # update form
        wd.find_element_by_name("update").click()
        self.open_contact_page()

    def edit_contact(self, contact_name):
        wd = self.ab.wd
        checkbox = self.locate(contact_name)
        contact_id = wd.find_element_by_xpath(checkbox).get_attribute("id")
        edit_button = '//a[@href = "edit.php?id=' + contact_id + '"]/img'
        wd.find_element_by_xpath(edit_button).click()

    def delete_from_edit(self, contact_name):
        wd = self.ab.wd
        self.open_contact_page()
        self.edit_contact(contact_name)
        # delete contact
        wd.find_element_by_xpath('//input[@value = "Delete"]').click()
        self.open_contact_page()

    def delete_from_home(self, contact_name):
        wd = self.ab.wd
        self.open_contact_page()
        checkbox = self.locate(contact_name)
        wd.find_element_by_xpath(checkbox).click()
        wd.find_element_by_xpath('//input[@value = "Delete"]').click()
        self.open_contact_page()

    def count(self):
        wd = self.ab.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def exists(self, contact_name):
        wd = self.ab.wd
        self.open_contact_page()
        checkbox = self.locate(contact_name)
        if len(wd.find_elements_by_xpath(checkbox))>0:
            return True
        else:
            return False

    def locate(self, contact_name):
        return '//input [@name="selected[]" and contains(@title,"' + contact_name + '")]'

    def get_contact_list(self):
        wd = self.ab.wd
        self.open_contact_page()
        contacts = []
        rows = wd.find_elements_by_css_selector("tr")
        i = len(rows)
        for element in rows:
            #wd.find_elements_by_xpath('//tbody/tr [@class = "" or @class = "odd"]'):
            # #wd.find_elements_by_xpath('//tr/td [@class = "center"]/input'):
            first_name = element.find_element_by_xpath("//tr[" + str(i) + "]/td[3]").text
            last_name = element.find_element_by_xpath("//tr[" + str(i) + "]/td[2]").text
            id_ = element.find_element_by_xpath("//tr[" + str(i) + "]/td[1]/input").get_attribute("id")
            contacts.append(Contact(firstname=first_name, id=id_, lastname=last_name))
            i = i - 1
            if i == 1:
                break
        return contacts






from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, ab):
        self.ab = ab

    def open_contact_page(self):
        wd = self.ab.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_xpath("//select[@name='group']/option[@value='']").click()


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
        self.contact_cache = None

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
        self.contact_cache = None

    def edit_by_index(self, index, contact_new, contact_page):
        wd = self.ab.wd
        self.open_contact_page()
        self.edit_contact_by_index(index)
        self.populate_contact_data(contact_new, contact_page)
        # update form
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def edit_by_id(self, id, contact_new, contact_page):
        wd = self.ab.wd
        self.open_contact_page()
        self.edit_contact_by_id(id)
        self.populate_contact_data(contact_new, contact_page)
        # update form
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None


    def locate(self, contact_name):
        return '//input [@name="selected[]" and contains(@title,"' + contact_name + '")]'

    def edit_contact(self, contact_name):
        wd = self.ab.wd
        checkbox = self.locate(contact_name)
        contact_id = wd.find_element_by_xpath(checkbox).get_attribute("id")
        edit_button = '//a[@href = "edit.php?id=' + contact_id + '"]/img'
        wd.find_element_by_xpath(edit_button).click()

    def edit_contact_by_id(self, id):
        wd = self.ab.wd
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def edit_contact_by_index(self, index):
        wd = self.ab.wd
        self.open_contact_page()
        contact_row = wd.find_elements_by_xpath('//tr[@name = "entry"]')[index]
        #click Edit button
        contact_row.find_element_by_xpath(".//td[8]").click()

    def view_contact_by_index(self, index):
        wd = self.ab.wd
        self.open_contact_page()
        contact_row = wd.find_elements_by_xpath('//tr[@name = "entry"]')[index]
        #click Edit button
        contact_row.find_element_by_xpath(".//td[7]").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.ab.wd
        self.edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname= firstname, lastname= lastname, id = id, address=address,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax,
                       email1=email1, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.ab.wd
        self.view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax)



    def delete_from_edit(self, contact_name):
        wd = self.ab.wd
        self.open_contact_page()
        self.edit_contact(contact_name)
        # delete contact
        self.delete_contact()
        self.open_contact_page()
        self.contact_cache = None

    def delete_contact(self):
        wd = self.ab.wd
        wd.find_element_by_xpath('//input[@value = "Delete"]').click()

    def delete_by_index_from_edit(self, index):
        wd = self.ab.wd
        self.open_contact_page()
        contact_row = wd.find_elements_by_xpath('//tr[@name = "entry"]')[index]
        # click Edit button
        contact_row.find_element_by_xpath(".//td[8]").click()
        self.delete_contact()
        self.open_contact_page()
        self.contact_cache = None

    def delete_by_id_from_edit(self, id):
        wd = self.ab.wd
        self.open_contact_page()
        self.edit_contact_by_id(id)
        self.delete_contact()
        self.open_contact_page()
        self.contact_cache = None



    def delete_from_home(self, contact_name):
        wd = self.ab.wd
        self.open_contact_page()
        checkbox = self.locate(contact_name)
        wd.find_element_by_xpath(checkbox).click()
        self.delete_contact()
        self.open_contact_page()
        self.contact_cache = None

    def delete_by_index_from_home(self, index):
        wd = self.ab.wd
        self.open_contact_page()
        contact_row = wd.find_elements_by_xpath('//tr[@name = "entry"]')[index]
        # select row
        contact_row.find_element_by_xpath(".//td[1]").click()
        self.delete_contact()
        self.open_contact_page()
        self.contact_cache = None

    def delete_by_id_from_home(self, id):
        wd = self.ab.wd
        self.open_contact_page()
        self.select_by_id(id)
        self.delete_contact()
        self.open_contact_page()
        self.contact_cache = None

    def select_by_id(self, id):
        wd = self.ab.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_by_id_and_edit(self, id):
        wd = self.ab.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

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

    def exists_any(self):
        wd = self.ab.wd
        self.open_contact_page()
        if len(wd.find_elements_by_xpath('//input [@name="selected[]"]'))>0:
            return True
        else:
            return False

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.ab.wd
            self.open_contact_page()
            self.contact_cache = []
            rows = wd.find_elements_by_xpath('//tr[@name = "entry"]')
            for element in rows:
                first_name = element.find_element_by_xpath('.//td[3]').text
                last_name = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_xpath(".//td[1]/input").get_attribute("id")
                address = element.find_element_by_xpath(".//td[4]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                self.contact_cache.append(Contact(firstname=first_name, id=id, lastname=last_name, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def add_to_group(self,id,group_id):
        wd = self.ab.wd
        self.open_contact_page()
        self.select_by_id(id)
        self.select_group_to_add(group_id)
        self.open_contact_page()

    def select_group_to_add(self, group_id):
        wd = self.ab.wd
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group_id).click()
        wd.find_element_by_xpath("//input[@type='submit' and @value='Add to']").click()

    def remove_from_group(self, contact_id, group_id):
        wd = self.ab.wd
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group_id).click()
        self.select_by_id(contact_id)
        wd.find_element_by_xpath("//input[@type='submit' and @name='remove']").click()
        self.open_contact_page()








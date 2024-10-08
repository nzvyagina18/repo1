from model.group import Group


class GroupHelper:
    def __init__(self, ab):
        self.ab = ab

    def open_groups_page(self):
        wd = self.ab.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.ab.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # Open Groups page
        wd = self.ab.wd
        self.open_groups_page()
        self.create_group()
        self.populate_group_data(group)
        self.submit_form()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def submit_form(self):
        # submit form
        wd = self.ab.wd
        wd.find_element_by_name("submit").click()

    def create_group(self):
        # initiate group creation
        wd = self.ab.wd
        wd.find_element_by_name("new").click()

    def populate_group_data(self, group):
        wd = self.ab.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.ab.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.ab.wd
        self.open_groups_page()
        self.select_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.ab.wd
        self.open_groups_page()
        self.select_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_by_index(self, index):
        wd = self.ab.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.ab.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete(self, group_name):
        wd = self.ab.wd
        self.open_groups_page()
        checkbox = '//input [@name="selected[]" and contains(@title,"' + group_name + '")]'
        wd.find_element_by_xpath(checkbox).click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit(self, group_name, group):
        # Open Groups page
        wd = self.ab.wd
        self.open_groups_page()
        self.edit_group(group_name)
        self.populate_group_data(group)
        # submit form
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def edit_by_index(self, index, new_group_data):
        # Open Groups page
        wd = self.ab.wd
        self.open_groups_page()
        self.select_by_index(index)
        wd.find_element_by_name("edit").click()
        self.populate_group_data(new_group_data)
        # submit form
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def edit_by_id(self, id, new_group_data):
        # Open Groups page
        wd = self.ab.wd
        self.open_groups_page()
        self.select_by_id(id)
        wd.find_element_by_name("edit").click()
        self.populate_group_data(new_group_data)
        # submit form
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group(self, group_name):
        wd = self.ab.wd
        self.select(group_name)
        # initiate group editing
        wd.find_element_by_name("edit").click()

    def select(self, group_name):
        wd = self.ab.wd
        checkbox = '//input [@name="selected[]" and contains(@title,"' + group_name + '")]'
        wd.find_element_by_xpath(checkbox).click()

    def count(self):
        wd = self.ab.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def exists(self, group_name):
        wd = self.ab.wd
        self.open_groups_page()
        checkbox = '//input [@name="selected[]" and contains(@title,"' + group_name + '")]'
        return len(wd.find_elements_by_xpath(checkbox))

    group_cache = None
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.ab.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)





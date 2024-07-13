class GroupHelper:
    def __init__(self, ab):
        self.ab = ab

    def open_groups_page(self):
        wd = self.ab.wd
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.ab.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # Open Groups page
        wd = self.ab.wd
        self.open_groups_page()
        self.create_group(wd)
        self.populate_group_data(group, wd)
        self.submit_form(wd)
        # return to groups page
        self.return_to_groups_page()

    def submit_form(self, wd):
        # submit form
        wd.find_element_by_name("submit").click()

    def create_group(self, wd):
        # initiate group creation
        wd.find_element_by_name("new").click()

    def populate_group_data(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first(self):
        wd = self.ab.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def delete(self, group_name):
        wd = self.ab.wd
        self.open_groups_page()
        checkbox = '//input [@name="selected[]" and contains(@title,"' + group_name + '")]'
        wd.find_element_by_xpath(checkbox).click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit(self, group_name, group):
        # Open Groups page
        wd = self.ab.wd
        self.open_groups_page()
        self.edit_group(group_name, wd)
        self.populate_group_data(group, wd)
        # submit form
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()

    def edit_group(self, group_name, wd):
        self.select(group_name)
        # initiate group editing
        wd.find_element_by_name("edit").click()

    def select(self, group_name):
        wd = self.ab.wd
        checkbox = '//input [@name="selected[]" and contains(@title,"' + group_name + '")]'
        wd.find_element_by_xpath(checkbox).click()


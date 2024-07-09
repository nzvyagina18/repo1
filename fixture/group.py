

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

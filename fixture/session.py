class SessionHelper:
    def __init__(self, ab):
        self.ab = ab
    def login(self, user, password):
        wd = self.ab.wd
        self.ab.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.ab.wd
        wd.find_element_by_link_text("Logout").click()
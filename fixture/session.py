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
        wd.find_element_by_name("user")

    def is_logged_in(self):
        wd = self.ab.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_logout(self):
        wd = self.ab.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in_as(self, username):
        wd = self.ab.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        wd = self.ab.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)





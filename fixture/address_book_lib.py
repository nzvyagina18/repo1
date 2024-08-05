from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
#from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class AddressBook:
    def __init__(self, browser, base_url, login, password):

        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        #self.wd = webdriver.Firefox(executable_path=r'geckodriver.exe',
        #                            options=options)
        #self.wd.implicitly_wait(10)
        #self.wd.WebDriver() #this code does not work for me
        #self.session = SessionHelper(self)
        #self.group = GroupHelper(self)
        #self.contact = ContactHelper(self)

        if browser == 'firefox':
            self.wd = webdriver.Firefox(executable_path=r'geckodriver.exe',
                                        options=options)
        elif browser == 'chrome':
            self.wd = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'ie':
            self.wd = webdriver.Ie(IEDriverManager().install())
        else:
            raise ValueError("Unrecognized browser %s", browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.login = login
        self.password = password

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


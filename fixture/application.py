from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    # Auxiliary

    def set_value_to_element(self, name, value):
        wd = self.wd
        element = wd.find_element_by_name(name)
        element.click()
        element.clear()
        element.send_keys(value)

    # Home page

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # Checks

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    # Teardown

    def destroy(self):
        self.wd.quit()
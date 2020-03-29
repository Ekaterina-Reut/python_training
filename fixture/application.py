from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

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

    def go_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    # Groups

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.set_value_to_element(name="group_name", value=group.name)
        self.set_value_to_element(name="group_header", value=group.header)
        self.set_value_to_element(name="group_footer", value=group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    # Contacts

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_add_contact_page()
        # input general info
        self.set_value_to_element(name="firstname", value=contact.first_name)
        self.set_value_to_element(name="middlename", value=contact.middle_name)
        self.set_value_to_element(name="lastname", value=contact.last_name)
        self.set_value_to_element(name="nickname", value=contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        self.set_value_to_element(name="title", value=contact.contact_title)
        self.set_value_to_element(name="company", value=contact.company)
        self.set_value_to_element(name="address", value=contact.address)
        self.set_value_to_element(name="home", value=contact.phone_home)
        self.set_value_to_element(name="mobile", value=contact.phone_mobile)
        self.set_value_to_element(name="work", value=contact.phone_work)
        self.set_value_to_element(name="fax", value=contact.fax)
        self.set_value_to_element(name="email", value=contact.email)
        self.set_value_to_element(name="email2", value=contact.email2)
        self.set_value_to_element(name="email3", value=contact.email3)
        self.set_value_to_element(name="homepage", value=contact.homepage)
        # input birthday date
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_xpath("//option[@value='11']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_xpath("//option[@value='September']").click()
        self.set_value_to_element(name="byear", value=contact.birth_year)
        # input anniversary date
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_xpath("(//option[@value='17'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        self.set_value_to_element(name="ayear", value=contact.anniversary_year)
        # input secondary info
        self.set_value_to_element(name="address2", value=contact.address2)
        self.set_value_to_element(name="phone2", value=contact.home2)
        self.set_value_to_element(name="notes", value=contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # go to home page
        self.go_to_home_page()

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
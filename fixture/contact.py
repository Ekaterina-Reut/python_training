from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # input general info
        self.app.set_value_to_element(name="firstname", value=contact.first_name)
        self.app.set_value_to_element(name="middlename", value=contact.middle_name)
        self.app.set_value_to_element(name="lastname", value=contact.last_name)
        self.app.set_value_to_element(name="nickname", value=contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        self.app.set_value_to_element(name="title", value=contact.contact_title)
        self.app.set_value_to_element(name="company", value=contact.company)
        self.app.set_value_to_element(name="address", value=contact.address)
        self.app.set_value_to_element(name="home", value=contact.phone_home)
        self.app.set_value_to_element(name="mobile", value=contact.phone_mobile)
        self.app.set_value_to_element(name="work", value=contact.phone_work)
        self.app.set_value_to_element(name="fax", value=contact.fax)
        self.app.set_value_to_element(name="email", value=contact.email)
        self.app.set_value_to_element(name="email2", value=contact.email2)
        self.app.set_value_to_element(name="email3", value=contact.email3)
        self.app.set_value_to_element(name="homepage", value=contact.homepage)
        # input birthday date
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_xpath("//option[@value='11']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_xpath("//option[@value='September']").click()
        self.app.set_value_to_element(name="byear", value=contact.birth_year)
        # input anniversary date
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_xpath("(//option[@value='17'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        self.app.set_value_to_element(name="ayear", value=contact.anniversary_year)
        # input secondary info
        self.app.set_value_to_element(name="address2", value=contact.address2)
        self.app.set_value_to_element(name="phone2", value=contact.home2)
        self.app.set_value_to_element(name="notes", value=contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # go to home page
        self.go_to_home_page()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
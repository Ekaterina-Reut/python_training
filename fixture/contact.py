from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_edin_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_contact_details(self, contact):
        wd = self.app.wd
        # input general info
        self.app.change_field_value(name="firstname", value=contact.first_name)
        self.app.change_field_value(name="middlename", value=contact.middle_name)
        self.app.change_field_value(name="lastname", value=contact.last_name)
        self.app.change_field_value(name="nickname", value=contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        self.app.change_field_value(name="title", value=contact.contact_title)
        self.app.change_field_value(name="company", value=contact.company)
        self.app.change_field_value(name="address", value=contact.address)
        self.app.change_field_value(name="home", value=contact.phone_home)
        self.app.change_field_value(name="mobile", value=contact.phone_mobile)
        self.app.change_field_value(name="work", value=contact.phone_work)
        self.app.change_field_value(name="fax", value=contact.fax)
        self.app.change_field_value(name="email", value=contact.email)
        self.app.change_field_value(name="email2", value=contact.email2)
        self.app.change_field_value(name="email3", value=contact.email3)
        self.app.change_field_value(name="homepage", value=contact.homepage)
        # input birthday date
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_xpath("//option[@value='11']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_xpath("//option[@value='September']").click()
        self.app.change_field_value(name="byear", value=contact.birth_year)
        # input anniversary date
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_xpath("(//option[@value='17'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        self.app.change_field_value(name="ayear", value=contact.anniversary_year)
        # input secondary info
        self.app.change_field_value(name="address2", value=contact.address2)
        self.app.change_field_value(name="phone2", value=contact.home2)
        self.app.change_field_value(name="notes", value=contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_details(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # go to home page
        self.go_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # wait page with message for correct full deletion before next checks
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".msgbox")))
        # go to home page
        self.go_to_home_page()
        self.contact_cache = None

    def delete_first_contact_on_edit_page(self):
        self.delete_contact_on_edit_page_by_index(0)

    def delete_contact_on_edit_page_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        self.open_edin_contact_page()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        # go to home page
        self.go_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        self.open_edin_contact_page()
        # edit contact information
        self.fill_contact_details(contact)
        # submit updating
        wd.find_element_by_name("update").click()
        # go to home page
        self.go_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                last_name_value = element.find_element_by_xpath(".//td[2]").text
                first_name_value = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, last_name=last_name_value, first_name=first_name_value))
        return list(self.contact_cache)

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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

    def open_contact_edit_page_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_css_selector("img[alt='Details']")[index].click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_contact_details(self, contact):
        wd = self.app.wd
        # input general info
        self.app.change_field_value(name="firstname", value=contact.first_name)
        self.app.change_field_value(name="middlename", value=contact.middle_name)
        self.app.change_field_value(name="lastname", value=contact.last_name)
        self.app.change_field_value(name="nickname", value=contact.nickname)
        if contact.photo is not None:
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
        if contact.birth_day is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        if contact.birth_month is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        self.app.change_field_value(name="byear", value=contact.birth_year)
        # input anniversary date
        if contact.anniversary_day is not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        if contact.anniversary_month is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        self.app.change_field_value(name="ayear", value=contact.anniversary_year)
        # input secondary info
        self.app.change_field_value(name="address2", value=contact.address2)
        self.app.change_field_value(name="phone2", value=contact.phone_home2)
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
        self.open_contact_edit_page_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        # go to home page
        self.go_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
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
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                last_name_value = cells[1].text
                first_name_value = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, last_name=last_name_value, first_name=first_name_value,
                                                  address=address, all_emails_from_homepage =all_emails,
                                                  all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        print(firstname, lastname, id, homephone, workphone, mobilephone, secondaryphone)
        return Contact(id=id, first_name=firstname, last_name=lastname,
                       address=address, email=email1, email2=email2, email3=email3,
                       phone_home=homephone, phone_mobile=mobilephone,
                       phone_work=workphone, phone_home2=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(phone_home=homephone, phone_mobile=mobilephone,
                       phone_work=workphone, phone_home2=secondaryphone)


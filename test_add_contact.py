# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_add_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def set_value_to_element(self, wd, name, value):
        element = wd.find_element_by_name(name)
        element.click()
        element.clear()
        element.send_keys(value)

    def create_contact(self, wd, contact):
        # input general info
        self.set_value_to_element(wd, name="firstname", value=contact.first_name)
        self.set_value_to_element(wd, name="middlename", value=contact.middle_name)
        self.set_value_to_element(wd, name="lastname", value=contact.last_name)
        self.set_value_to_element(wd, name="nickname", value=contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        self.set_value_to_element(wd, name="title", value=contact.contact_title)
        self.set_value_to_element(wd, name="company", value=contact.company)
        self.set_value_to_element(wd, name="address", value=contact.address)
        self.set_value_to_element(wd, name="home", value=contact.phone_home)
        self.set_value_to_element(wd, name="mobile", value=contact.phone_mobile)
        self.set_value_to_element(wd, name="work", value=contact.phone_work)
        self.set_value_to_element(wd, name="fax", value=contact.fax)
        self.set_value_to_element(wd, name="email", value=contact.email)
        self.set_value_to_element(wd, name="email2", value=contact.email2)
        self.set_value_to_element(wd, name="email3", value=contact.email3)
        self.set_value_to_element(wd, name="homepage", value=contact.homepage)
        # input birthday date
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_xpath("//option[@value='11']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_xpath("//option[@value='September']").click()
        self.set_value_to_element(wd, name="byear", value=contact.birth_year)
        # input anniversary date
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_xpath("(//option[@value='17'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        self.set_value_to_element(wd, name="ayear", value=contact.anniversary_year)
        # input secondary info
        self.set_value_to_element(wd, name="address2", value=contact.address2)
        self.set_value_to_element(wd, name="phone2", value=contact.home2)
        self.set_value_to_element(wd, name="notes", value=contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def go_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

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

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd, Contact(first_name="Tre", middle_name="Hgf", last_name="Wfd", nickname="Jhfg",
                                        photo="D:\\work\\img1200.jpg", contact_title="T title", company="T Company",
                                        address="T address", phone_home="745", phone_mobile="584", phone_work="658",
                                        fax="987", email="email@1", email2="email@2", email3="email@3",
                                        homepage="t hpage", birth_day="11", birth_month="September", birth_year="1975",
                                        anniversary_day="17", anniversary_month="October", anniversary_year="2016",
                                        address2="S Address", home2="S home", notes="S Notes"))
        self.go_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

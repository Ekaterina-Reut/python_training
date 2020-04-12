# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                   birth_month="September", birth_year="1975", anniversary_day="17",
                                   anniversary_month="October", anniversary_year="2016"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_first_contact_in_edit_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                   birth_month="September", birth_year="1975", anniversary_day="17",
                                   anniversary_month="October", anniversary_year="2016"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_on_edit_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

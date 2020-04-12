# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                   birth_month="September", birth_year="1975", anniversary_day="17",
                                   anniversary_month="October", anniversary_year="2016"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_delete_some_contact_in_edit_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                   birth_month="September", birth_year="1975", anniversary_day="17",
                                   anniversary_month="October", anniversary_year="2016"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_on_edit_page_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

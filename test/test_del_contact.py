# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                   birth_month="September", birth_year="1975", anniversary_day="17",
                                   anniversary_month="October", anniversary_year="2016"))
    app.contact.delete_first_contact()


def test_delete_first_contact_in_edit_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                   birth_month="September", birth_year="1975", anniversary_day="17",
                                   anniversary_month="October", anniversary_year="2016"))
    app.contact.delete_first_contact_on_edit_page()
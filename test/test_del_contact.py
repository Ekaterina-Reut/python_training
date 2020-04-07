# -*- coding: utf-8 -*-
def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_delete_first_contact_in_edit_form(app):
    app.contact.delete_first_contact_on_edit_page()
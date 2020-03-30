# -*- coding: utf-8 -*-
def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_first_contact_in_edit_form(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_on_edit_page()
    app.session.logout()
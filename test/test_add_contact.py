# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('When I add a contact %s to the list' % contact):
        app.contact.create(contact)
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        # assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact(app, json_contacts):
#     contact = json_contacts
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

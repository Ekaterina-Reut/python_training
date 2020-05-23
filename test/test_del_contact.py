# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import allure


def test_delete_some_contact(app, db, check_ui):
    with allure.step('Add contact if contact list is empty'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
                                       birth_month="September", birth_year="1975", anniversary_day="17",
                                       anniversary_month="October", anniversary_year="2016"))
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When delete the contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_delete_some_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
#                                    birth_month="September", birth_year="1975", anniversary_day="17",
#                                    anniversary_month="October", anniversary_year="2016"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts

# def test_delete_some_contact_in_edit_form(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="11",
#                                    birth_month="September", birth_year="1975", anniversary_day="17",
#                                    anniversary_month="October", anniversary_year="2016"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_on_edit_page_by_index(index)
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts

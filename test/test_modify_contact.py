# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact for edit", photo="D:\\work\\img1200.jpg", birth_day="15",
                                   birth_month="October", birth_year="1945", anniversary_day="21",
                                   anniversary_month="September", anniversary_year="2010"))
    old_contacts = db.get_contact_list()
    contact_old = random.choice(old_contacts)
    contact_new = Contact(id=contact_old.id, first_name="1Tre", middle_name="1Hgf",
                         last_name="1Wfd", nickname="1Jhfg", contact_title="1T title",
                         company="1T Company", address="1T address", phone_home="1456",
                         phone_mobile="123", phone_work="1345", fax="1987", email="1email@1",
                         email2="1email@2", email3="1email@3", homepage="1t hpage", birth_day="12",
                         birth_month="September", birth_year="1934", anniversary_day="23",
                         anniversary_month="October", anniversary_year="2007",
                         address2="1S Address", phone_home2="1S home", notes="1S Notes")
    app.contact.edit_contact_by_id(contact_old.id, contact_new)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_old)
    old_contacts.append(contact_new)
    assert sorted(old_contacts, key=Contact.id_or_max) == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


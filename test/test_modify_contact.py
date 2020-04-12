# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for delete", photo="D:\\work\\img1200.jpg", birth_day="15",
                                   birth_month="October", birth_year="1945", anniversary_day="21",
                                   anniversary_month="September", anniversary_year="2010"))
    old_contacts = app.contact.get_contact_list()
    contact_name = Contact(first_name="1Tre", last_name="1Wfd")
    contact_name.id = old_contacts[0].id
    app.contact.edit_first_contact(Contact(first_name=contact_name.first_name, middle_name="1Hgf",
                                           last_name=contact_name.last_name, nickname="1Jhfg",
                                           photo="D:\\work\\img1200.jpg", contact_title="1T title",
                                           company="1T Company",address="1T address", phone_home="1456",
                                           phone_mobile="123", phone_work="1345", fax="1987", email="1email@1",
                                           email2="1email@2", email3="1email@3", homepage="1t hpage", birth_day="12",
                                           birth_month="September", birth_year="1934", anniversary_day="23",
                                           anniversary_month="October", anniversary_year="2007",
                                           address2="1S Address", home2="1S home", notes="1S Notes"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact_name
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
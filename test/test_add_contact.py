# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Tre", middle_name="Hgf", last_name="Wfd", nickname="Jhfg",
                                    photo="D:\\work\\img1200.jpg", contact_title="T title", company="T Company",
                                    address="T address", phone_home="745", phone_mobile="584", phone_work="658",
                                    fax="987", email="email@1", email2="email@2", email3="email@3",
                                    homepage="t hpage", birth_day="11", birth_month="September", birth_year="1975",
                                    anniversary_day="17", anniversary_month="October", anniversary_year="2016",
                                    address2="S Address", home2="S home", notes="S Notes"))
    app.session.logout()

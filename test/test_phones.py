import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_homepage(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.phone_home2 == contact_from_edit_page.phone_home2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                      [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone_home2]))))

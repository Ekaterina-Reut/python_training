def test_contact_info_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for page in contacts_from_home_page:
        for db in contacts_from_db:
            if page.id == db.id:
                assert page.last_name == db.last_name
                assert page.first_name == db.first_name
                assert page.address == db.address
                assert page.all_emails_from_homepage == db.all_emails
                assert page.all_phones_from_homepage == db.all_phones

# def test_contact_info_on_home_page(app):
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.last_name == contact_from_edit_page.last_name
#     assert contact_from_home_page.first_name == contact_from_edit_page.first_name
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_emails_from_homepage == contact_from_edit_page.all_emails
#     assert contact_from_home_page.all_phones_from_homepage == contact_from_edit_page.all_phones
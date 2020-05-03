from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from random import randrange


def test_add_contact_to_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    # Проверить есть ли группы, если нет, то создать
    groups_list = db.get_group_list()
    if len(groups_list) == 0:
        app.group.create(Group(name='For add contact'))
        groups_list = db.get_group_list()

    # Выбрать группу
    group = groups_list[randrange(len(groups_list))]

    # Выбрать контакт не из группы, если нет, то создать
    contacts_list = db.get_contacts_not_in_group(group)
    if len(contacts_list) == 0:
        app.contact.create(Contact(first_name="Contact for group"))
        contacts_list = db.get_contacts_not_in_group(group)

    contact = contacts_list[randrange(len(contacts_list))]
    old_contacts_in_group = db.get_contacts_in_group(group)

    app.contact.add_contact_to_group(contact.id, group.id)

    old_contacts_in_group.append(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)




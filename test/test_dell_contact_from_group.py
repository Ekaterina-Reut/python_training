from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from random import randrange


def test_dell_contact_from_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    # Проверить есть ли группы, если нет, то создать
    groups_list = db.get_group_list()
    if len(groups_list) == 0:
        app.group.create(Group(name='For dell contact'))
        groups_list = db.get_group_list()

    # Выбрать группу
    group = groups_list[randrange(len(groups_list))]

    # Выбрать контакт из группы, если нет, то добавит в группу
    contacts_in_gr = db.get_contacts_in_group(group)
    if len(contacts_in_gr) == 0:
        contacts_not_in_gr = db.get_contacts_not_in_group(group)
        # Если и контактов нет, то создаём
        if len(contacts_not_in_gr) == 0:
            app.contact.create(Contact(first_name="Contact for group dell"))
            contacts_not_in_gr = db.get_contacts_not_in_group(group)
        contact_to_gr = contacts_not_in_gr[randrange(len(contacts_not_in_gr))]
        app.contact.add_contact_to_group(contact_to_gr.id, group.id)
        contacts_in_gr = db.get_contacts_in_group(group)

    contact = contacts_in_gr[randrange(len(contacts_in_gr))]
    old_contacts_in_group = db.get_contacts_in_group(group)

    app.contact.remove_contact_from_group(contact.id, group.id)

    old_contacts_in_group.remove(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)




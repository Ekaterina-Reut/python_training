from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_in_group(Group(id=262))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass



# try:
#     l = db.get_contacts_not_in_group(Group(id="244"))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass


# try:
#     l = db.get_contacts_in_group(Group(id="244"))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass


# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass



# from fixture.db import DbFixture
#
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()
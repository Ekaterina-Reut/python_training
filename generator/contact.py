from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10 + "@"*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10 + "\n"*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_string(prefix, maxlen):
    symbols = string.punctuation + " "*10 + string.digits*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_date():
    return str(random.randrange(1, 31))


def random_month():
    months = ("January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December")
    return random.choice(months)


def random_year():
    return str(random.randrange(1000, 2021))


def random_photo():
    return "D:\\work\\%s.jpg" % (random.randrange(11,17))


testdata = [Contact(first_name="", middle_name="", last_name="",
                   nickname="", photo="", contact_title="",
                   company="", address="", phone_home="", phone_mobile="",
                   phone_work="", fax="", email="", email2="", email3="",
                   homepage="", birth_day="", birth_month="", birth_year="",
                   anniversary_day="", anniversary_month="", anniversary_year="",
                   address2="", phone_home2="", notes="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 15),
            last_name=random_string("last_name", 10), nickname=random_string("nickname", 10), photo=random_photo(),
            contact_title=random_string("contact_title", 10), company=random_string("company", 20),
            address=random_address_string("address", 40), phone_home=random_phone_string("phone_h", 15),
            phone_mobile=random_phone_string("phone_m", 15), phone_work=random_phone_string("phone_w", 15),
            fax=random_phone_string("fax", 15), email=random_email_string("email", 30),
            email2=random_email_string("email2", 30), email3=random_email_string("email3", 30),
            homepage=random_string("homepage", 20), birth_day=random_date(), birth_month=random_month(),
            birth_year=random_year(), anniversary_day=random_date(), anniversary_month=random_month(),
            anniversary_year=random_year(), address2=random_address_string("address2", 40),
            phone_home2=random_phone_string("phone_h2", 15), notes=random_address_string("notes", 40))
    for name in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
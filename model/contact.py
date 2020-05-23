from sys import maxsize
import re


class Contact:

    def __init__(self,
                 first_name=None,
                 middle_name=None,
                 last_name=None,
                 nickname=None,
                 photo=None,
                 contact_title=None,
                 company=None,
                 address=None,
                 phone_home=None,
                 phone_mobile=None,
                 phone_work=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 birth_day=None,
                 birth_month=None,
                 birth_year=None,
                 anniversary_day=None,
                 anniversary_month=None,
                 anniversary_year=None,
                 address2=None,
                 phone_home2=None,
                 notes=None,
                 id=None,
                 all_phones_from_homepage=None,
                 all_emails_from_homepage=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo = photo
        self.contact_title = contact_title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.phone_home2 = phone_home2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage
        self.all_phones = self.merge_phones_like_homepage()
        self.all_emails = self.merge_emails_like_homepage()

    def __repr__(self):
        return "%s:%s, %s, %s, %s" % (self.id, self.last_name, self.first_name,
                                              self.all_phones_from_homepage, self.all_emails_from_homepage)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.last_name == other.last_name and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_homepage(self):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                          [self.phone_home, self.phone_mobile, self.phone_work, self.phone_home2]))))

    def merge_emails_like_homepage(self):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None, [self.email, self.email2, self.email3])))

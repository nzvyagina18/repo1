from sys import maxsize


class Contact:
    def __init__(self, firstname=None, nickname=None, lastname=None, midname=None, title=None, company=None, address=None, homephone=None, mobilephone=None,
                    workphone=None, fax=None, all_phones_from_home_page=None, all_emails_from_home_page=None, email1=None, email2=None, email3=None, homepage=None, birthdate=None, ann_date=None, photo_path=None, id=None):
        self.firstname = firstname
        self.nickname = nickname
        self.lastname = lastname
        self.midname = midname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthdate = birthdate
        self.ann_date = ann_date
        self.photo = photo_path
        self.id = id

    def __repr__(self):
        return "%s;%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.homephone, self.address)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address
                and self.all_emails_from_home_page == other.all_emails_from_home_page and self.all_phones_from_home_page == other.all_phones_from_home_page)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

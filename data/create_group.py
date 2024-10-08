from model.group import Group
import random
import string

constant = [
    Group(name="name1",header="header1",footer="footer1"),
    Group(name="name2",header="header2",footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata2 = [Group("", "", "")] + [
    Group(name=random_string("name", 10), header = random_string("header", 20), footer = random_string("header", 20))
    for i in range(5)
]

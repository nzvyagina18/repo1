# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group("", "", "")] + [
    Group(name=random_string("name", 10), header = random_string("header", 20), footer = random_string("header", 20))
    for i in range(5)
]
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_create_group(a_b, group):
    old_groups = a_b.group.get_group_list()
    a_b.group.create(group)
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) + 1 == a_b.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_create_empty_group(a_b):
    old_groups = a_b.group.get_group_list()
    group = Group("", "", "")
    a_b.group.create(group)
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) + 1 == a_b.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




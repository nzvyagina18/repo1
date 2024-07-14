# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(a_b):
    if a_b.group.exists('b3') > 0:
        a_b.group.create(Group(name = 'b3'))
    a_b.group.create(Group("b1", "bbb", "ccc"))


def test_create_empty_group(a_b):
    a_b.group.create(Group("", "", ""))

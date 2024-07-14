# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(a_b):
    a_b.group.create(Group("aaa", "bbb", "ccc"))
    a_b.session.logout()


def test_create_empty_group(a_b):
    a_b.group.create(Group("", "", ""))

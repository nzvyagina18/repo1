# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(a_b):
    a_b.group.create(Group("aaa", "bbb", "ccc"))


def test_create_empty_group(a_b):
    a_b.group.create(Group("", "", ""))

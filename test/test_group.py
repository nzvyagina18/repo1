# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(a_b):
    old_groups = a_b.group.get_group_list()
    a_b.group.create(Group("b1", "bbb", "ccc"))
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_create_empty_group(a_b):
    old_groups = a_b.group.get_group_list()
    a_b.group.create(Group("", "", ""))
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

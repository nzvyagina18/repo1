# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize


def test_create_group(a_b):
    old_groups = a_b.group.get_group_list()
    group = Group("b1", "bbb", "ccc")
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
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




# -*- coding: utf-8 -*-
from model.group import Group
#from sys import maxsize
#import pytest
#from data.create_group import constant as testdata


def test_create_group(a_b, data_groups):
    group = data_groups
    old_groups = a_b.group.get_group_list()
    a_b.group.create(group)
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) + 1 == a_b.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_create_group_json(a_b, json_groups):
    group = json_groups
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




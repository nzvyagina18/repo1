# -*- coding: utf-8 -*-
from model.group import Group
#from sys import maxsize
#import pytest
#from data.create_group import constant as testdata


def test_create_group(a_b, data_groups, db, check_ui):
    group = data_groups
    old_groups = db.get_group_list()
    a_b.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)


def test_create_group_json(a_b, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    a_b.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)


def test_create_empty_group(a_b, db, check_ui):
    old_groups = db.get_group_list()
    group = Group("", "", "")
    a_b.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)




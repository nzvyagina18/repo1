from model.group import Group
from random import randrange
import random


def test_edit_group(a_b, db, check_ui):
    group_to_edit = 'b6'
    if a_b.group.exists(group_to_edit) == 0:
        a_b.group.create(Group(name = group_to_edit))
    old_groups = db.get_group_list()
    group = Group( name=group_to_edit + '_updated')
    for el in old_groups:
        if el.name == group_to_edit:
            group.id = el.id
            break
    a_b.group.edit(group_to_edit, group)
    new_groups = db.get_group_list()
    for el in old_groups:
        if el.id == group.id:
            el.name = group.name
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)


def test_edit_some_group(a_b, db, check_ui):
    if len(db.get_group_list()) == 0:
        a_b.group.create(Group(name = 'test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group( name='newly_updated_name')
    a_b.group.edit_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    for el in old_groups:
        if el.id == group.id:
            el.name = new_group_data.name
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_name(a_b):
    if a_b.group.exists('b2') == 0:
        a_b.group.create(Group(name = 'b2'))
    old_groups = a_b.group.get_group_list()
    a_b.group.edit('b2', Group(name='a111'))
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) == a_b.group.count()


def test_edit_group_header(a_b):
    if a_b.group.exists('b3') == 0:
        a_b.group.create(Group(name = 'b3'))
    old_groups = a_b.group.get_group_list()
    a_b.group.edit('b3', Group(header="bbb1header"))
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) == a_b.group.count()

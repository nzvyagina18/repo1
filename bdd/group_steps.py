from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header>, <footer>')
def new_group(name, header, footer):
    return Group(name, header, footer)

@when('I add the group to the list')
def add_new_group(a_b, new_group):
    a_b.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_list(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given('a non-empty group list')
def non_empty_group_list(db, a_b):
    if len(db.get_group_list()) == 0:
        a_b.group.create(Group(name='some name'))
    return db.get_group_list()

@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(a_b, random_group):
    a_b.group.delete_by_id(random_group.id)

@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, a_b, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)







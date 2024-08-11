from model.group import Group
from random import randrange
import random
def test_delete_first_group(a_b, db):
    if len(db.get_group_list()) == 0:
        a_b.group.create(Group(name = 'uuu'))
    old_groups = a_b.group.get_group_list()
    a_b.group.delete_first()
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) - 1 == a_b.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_some_group(a_b, db, check_ui):
    if len(db.get_group_list()) == 0:
        a_b.group.create(Group(name='uuu'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    a_b.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(a_b.group.get_group_list(), key=Group.id_or_max)

def test_delete_group(a_b):
    if a_b.group.exists('to_delete') == 0:
        a_b.group.create(Group(name = 'to_delete'))
    a_b.group.delete('to_delete')

from model.group import Group
from random import randrange
def test_delete_first_group(a_b):
    if a_b.group.count() == 0:
        a_b.group.create(Group(name = 'uuu'))
    old_groups = a_b.group.get_group_list()
    a_b.group.delete_first()
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) - 1 == a_b.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups

def test_delete_some_group(a_b):
    if a_b.group.count() == 0:
        a_b.group.create(Group(name = 'uuu'))
    old_groups = a_b.group.get_group_list()
    index = randrange(len(old_groups))
    a_b.group.delete_by_index(index)
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) - 1 == a_b.group.count()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

def test_delete_group(a_b):
    if a_b.group.exists('to_delete') == 0:
        a_b.group.create(Group(name = 'to_delete'))
    a_b.group.delete('to_delete')

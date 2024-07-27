from model.group import Group


def test_edit_group(a_b):
    group_to_edit = 'b6'
    if a_b.group.exists(group_to_edit) == 0:
        a_b.group.create(Group(name = group_to_edit))
    old_groups = a_b.group.get_group_list()
    group = Group( name=group_to_edit + '_updated')
    for el in old_groups:
        if el.name == group_to_edit:
            group.id = el.id
            break
    a_b.group.edit(group_to_edit, group)
    new_groups = a_b.group.get_group_list()
    assert len(old_groups) == a_b.group.count()
    for el in old_groups:
        if el.id == group.id:
            el.name = group.name
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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

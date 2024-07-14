from model.group import Group


def test_edit_group(a_b):
    if a_b.group.exists('b1') == 0:
        a_b.group.create(Group(name = 'b1'))
    a_b.group.edit('b1', Group( name='b1', header="bbb1", footer="ccc1"))


def test_edit_group_name(a_b):
    if a_b.group.exists('b2') == 0:
        a_b.group.create(Group(name = 'b2'))
    a_b.group.edit('b2', Group(name='a111'))


def test_edit_group_header(a_b):
    if a_b.group.exists('b3') == 0:
        a_b.group.create(Group(name = 'b3'))
    a_b.group.edit('b3', Group(header="bbb1header"))

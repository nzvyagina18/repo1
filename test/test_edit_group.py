from model.group import Group


def test_edit_group(a_b):
    a_b.group.edit('a1', Group( name='a1', header="bbb1", footer="ccc1"))
    a_b.session.logout()


def test_edit_group_name(a_b):
    a_b.group.edit('aaa1', Group(name='a111'))


def test_edit_group_header(a_b):
    a_b.group.edit('aaa1', Group(header="bbb1header"))

from model.group import Group


def test_edit_group(a_b):
    a_b.session.login( "admin", "secret")
    a_b.group.edit('a1', Group( name = 'a1', header = "bbb1", footer = "ccc1"))
    a_b.session.logout()
def test_delete_first_group(a_b):
    a_b.session.login( "admin", "secret")
    a_b.group.delete_first()
    a_b.session.logout()


def test_delete_group(a_b):
    a_b.session.login( "admin", "secret")
    a_b.group.delete('aaa')
    a_b.session.logout()

def test_delete_first_group(a_b):
    a_b.session.login( "admin", "secret")
    a_b.group.delete_first_group()
    a_b.session.logout()

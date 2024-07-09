def test_logout(a_b):
    a_b.session.login("admin", "secret")
    a_b.session.logout()

def test_logout2(a_b):
    a_b.session.login("admin", "secret")
    a_b.session.logout()

def test_logout3(a_b):
    a_b.session.login("admin", "secret")
    a_b.session.logout()

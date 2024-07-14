from model.group import Group
def test_delete_first_group(a_b):
    if a_b.group.count() == 0:
        a_b.group.create(Group(name = 'uuu'))
    a_b.group.delete_first()

def test_delete_group(a_b):
    if a_b.group.exists('to_delete') == 0:
        a_b.group.create(Group(name = 'to_delete'))
    a_b.group.delete('to_delete')

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    assert group
    if user in group.get_users():
        return True
    
    for parent_group in group.get_groups():
        return is_user_in_group(user, parent_group)
    
    return False


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, sub_child)) # True
    print(is_user_in_group(sub_child_user, child)) # True
    print(is_user_in_group(sub_child_user, parent)) # True

    # Edge case 1 - user empty
    print(is_user_in_group(None, parent)) # False

    # Edge case 2 - user not in group
    not_group = Group("not")
    print(is_user_in_group(sub_child_user, not_group)) # False

    # Edge case 3 - group empty
    try:
        print(is_user_in_group(sub_child_user, None))
    except AssertionError:
        pass

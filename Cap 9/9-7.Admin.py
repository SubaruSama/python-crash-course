'''
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.
'''

from user import User

class Privilege:
    '''
    9-8. Privileges: Write a separate Privileges class. The class should have one
    attribute, privileges , that stores a list of strings as described in Exercise 9-7.
    Move the show_privileges() method to this class. Make a Privileges instance
    as an attribute in the Admin class. Create a new instance of Admin and use your
    method to show its privileges.
    '''
    def __init__(self, privileges: list) -> None:
        self.privileges = privileges

    def show_privileges(self):
        print('The admin has those privileges:')
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name: str, last_name: str, nickname: str, email: str, privileges: list):
        super().__init__(first_name, last_name, nickname, email)
        self.privileges = Privilege(privileges)

admin = Admin(
    first_name='Carlos',
    last_name='Blanco',
    nickname='Sn0w',
    email='sn0w@sn0wnetwork.io',
    privileges= [
        'can add post',
        'can delete post',
        'can ban user',
        'maintace permissions',
        'modify user'
    ]
)

admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()
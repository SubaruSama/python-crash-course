'''
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0.
'''

from user import User

user1 = User(first_name='John', last_name='Johnny', nickname='JohnJohnny', email='john@johnnyemails.org')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f'Numbers of login attempt: {user1.get_quantity_login_attempts()}')
print('Flushing the counter of login attempts...')
user1.flush_login_attempts()
print(f'Numbers of login attempt: {user1.get_quantity_login_attempts()}')
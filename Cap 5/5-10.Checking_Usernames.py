'''
Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
Make a list of five or more usernames called current_users .
Make another list of five usernames called new_users . Make sure one or
two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.

'''

current_users = ['maria', 'joao', 'marcio', 'pedro', 'JOSE']
new_users = ['maria', 'bruna', 'bruno', 'fernando', 'Jose']

for new_user in new_users:
    for current_user in current_users:
        if current_user.capitalize == new_user.capitalize \
                or current_user.upper() == new_user.upper():
            print(f'Username {current_user} ja esta sendo usado')
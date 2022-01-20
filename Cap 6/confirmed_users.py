# Start with users that need to be verified,
# and a empty list to hold confirmed users.
# uncofirmed_users = ['alice', 'brian', 'candace']
uncofirmed_users = [
    {
        'name': 'alice',
        'confirmed': True
    },
    {
        'name': 'brian',
        'confirmed': True
    },
    {
        'name': 'candace',
        'confirmed': False
    }
]
confirmed_users = []
to_be_confirmed_users = []

while uncofirmed_users:
    current_user = uncofirmed_users.pop()

    if current_user['confirmed']:
        # print('User {user} confirmed' \
        #     .format(user=current_user['name']))
        confirmed_users.append(current_user)
    else:
        to_be_confirmed_users.append(current_user)

    # print('Verifying user: {current_user}' \
    #     .format(current_user=current_user.title()))
    # confirmed_users.append(current_user)

# Display all confirmed users.
print('Confirmed users: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.name)

print('\nUsers to be confirmed: ')
for to_be_confirmed_user in to_be_confirmed_users:
    print(to_be_confirmed_user['name'])
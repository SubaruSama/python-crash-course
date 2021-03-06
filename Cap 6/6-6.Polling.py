'''
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''

favorite_languages = {
    'rob': 'c++',
    'lfz': 'ruby',
    'desobediente civil': 'python',
    'snake': 'php',
    'formig4': 'python',
    'erika': ''
}

for key, value in favorite_languages.items():
    if value == '':
        print('-' * 5)
        print(f'{key} should take the poll!')
    else:
        print('-' * 5)
        print(f'{key} thanks for taking the poll!')
        print(f'{key} favorite language is {value}')

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and respose
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # Store the response in the dicionary:
    responses[name] = response
    # A chave vai ser o valor de name que ira conter o valor response dentro do dict responses

    # Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes / no)? ')
    if repeat == 'no':
        polling_active = False

# Pollin complete. Show the results.
print(responses)
print('\n--- Poll Results ---')
for name, response in responses.items():
    print('{name} would like to climb {response}' \
        .format(name=name, response=response))
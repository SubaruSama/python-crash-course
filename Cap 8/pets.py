def describe_pet(pet_name, animal_type='dog') -> None:
    '''
    Display information about a pet.
    '''
    print(f'\nI have a {animal_type}')
    print(f'My {animal_type} name is {pet_name.title()}')

describe_pet(pet_name='harry')
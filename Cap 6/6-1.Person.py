'''
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name , last_name , age , and city . Print each
piece of information stored in your dictionary.

'''
person = {
    'first_name': 'Aurora',
    'last_name': 'de Castro',
    'age': 20,
    'city': 'Porto Alegre'
}


print(
    'Nome: {first_name}\nSobrenome: {last_name} \
        \nIdade: {age}\nCidade: {city}'.format(
            first_name=person['first_name'],
            last_name=person['last_name'],
            age=person['age'],
            city=person['city']
    )
)

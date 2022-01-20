'''
Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
'''

rivers_country = {
    'parana': 'brasil',
    'mississipi': 'estados unidos',
    'danubio': 'alemanha'
}

for river, country in rivers_country.items():
    print(f'O rio {river.title()} percorre o {country.title()}.')

for river in rivers_country.keys():
    print(f'Rios: {river.title()}')

for country in rivers_country.values():
    print(f'Paises: {country.title()}')

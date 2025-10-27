people ={
    "first_name": ["Łukasz", "Jan", "Patryk"],
    "last_name": ["Kowalski", "Malinowski"]
}

people['address'] = ['Gdansk', 'Sopot']
print(people)

for key, values in people.items():
    print("Klucz: " + key)
    print("Wartości: ")
    for value in values:
        print("-" + value)
    print("#" * 10)

print(people.keys())
for key in people.keys():
    print(key)

for value in people.values():
    print(values)

print("#" * 20)

#########################################################
rows = [
    {"imie": "Brajanusz", "nazwisko": "Kopytko", "tel":123456789},
    {"imie": "Anżelika", "nazwisko": "Kłoda", "tel":222222222}
]

rows[0]['adres'] = 'Gdansk'
print(rows)
del rows[0]['adres']
print(rows)
print(rows[1]['imie'])

print("#" * 20)

for key, value in enumerate(rows):
    print(key, value)
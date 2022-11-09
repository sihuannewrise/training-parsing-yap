import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

result = []

for address in addresses:
    pattern = r'город.? (?P<town>\w+).*улиц.? (?P<street>\w+).*дом.? (?P<house>\d+).*квартир.? (?P<flat>\d+)'
    address_match = re.search(pattern, address)

    result.append(address_match.groups())

for row in result:
    print(*row)

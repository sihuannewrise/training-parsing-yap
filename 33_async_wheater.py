# def createGenerator(n):
#     for i in range(n):
#         yield f'{i**i} any str'


# for i in createGenerator(3):
#     print(i)

# import asyncio
# import time
# from aiohttp import ClientSession


# async def get_weather(city):
#     async with ClientSession() as session:
#         url = 'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             print(f'{city}: {weather_json["weather"][0]["main"]}')


# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))

#     for task in tasks:
#         await task


# cities = [
#     'Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#     'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York'
# ]

# print(time.strftime('%X'))

# asyncio.run(main(cities))

# print(time.strftime('%X'))


# import time
# import requests


# def get_weather(city):
#     url = 'http://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

#     weather_json = requests.get(url=url, params=params).json()
#     print(f'{city}: {weather_json["weather"][0]["main"]}')


# def main(cities_):
#     for city in cities_:
#         get_weather(city)


# cities = [
#     'Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#     'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York'
# ]

# print(time.strftime('%X'))

# main(cities)

# print(time.strftime('%X'))

import asyncio
import time
from aiohttp import ClientSession


async def get_weather(city):
    async with ClientSession() as session:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            return f'{city}: {weather_json["weather"][0]["main"]}'


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


cities = [
    'Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
    'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York'
]

print(time.strftime('%X'))

asyncio.run(main(cities))

print(time.strftime('%X'))

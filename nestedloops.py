""" Nested for loops
A nested loop is a loop inside another loop.
cities = ["Delhi", "Mumbai"]
years = [2024, 2025]

for city in cities:
    for year in years:
        print(city, year)
Output:
Delhi 2024
Delhi 2025
Mumbai 2024
Mumbai 2025
"""


cars = ["mercedes","bmw","audi"]
person = ["a","b","c"]

for car in  cars:
    for p in person:
        print(car,person)
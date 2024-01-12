

import random

facts = [
    "De hond is een roofdier uit de familie van de hondachtigen.",
    "De hond komt op alle continenten voor, meestal in gezelschap van de mens.",
    "Momenteel zijn er wereldwijd ongeveer 500 miljoen honden als huisdier.",
    "Al sinds duizenden jaren wordt de hond door mensen gebruikt, bijvoorbeeld bij de jacht, als herdershond, waakhond, trekdier of gezelschapsdier."
]

def get_random_fact():
    return random.choice(facts)

test = get_random_fact()
print(test)
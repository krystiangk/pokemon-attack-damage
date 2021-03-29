import requests
from math import prod


def get_data_from_api(pokemon_type):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{pokemon_type}/')
    return response.json()['damage_relations']


def findall(data, defender, damage):

    if isinstance(data, dict):
        for key in data:
            if key in damage.keys():
                findall(data[key], defender, damage[key])

    if isinstance(data, list):
        for key in data:
            if key['name'] in defender:
                damage.append(key['name'])

    return damage


def total_damage(damage):
    double = len(damage['double_damage_to'])
    half = len(damage['half_damage_to'])
    none = len(damage['no_damage_to'])

    total = (double * 2 if double > 0 else 1,
             half * 0.5 if half > 0 else 1,
             none * 0 if none > 0 else 1)

    print(total)
    if sum([double, half, none]) == 0:
        return 0
    else:
        return prod(total)


def get_attacker_and_defender(input_string):
    attacker, defender = list(map(lambda x: x.strip(), input_string.split("->")))
    defender = defender.split(" ")
    return attacker, defender


def pokemon_attack_damage(input_string):

    attacker, defender = get_attacker_and_defender(input_string)

    damage_relations = get_data_from_api(attacker)

    damage = {'double_damage_to': [],
               'half_damage_to': [],
               'no_damage_to': []
               }

    found_damage = findall(data=damage_relations, defender=defender, damage=damage)

    total = total_damage(found_damage)

    return f"{total}x"


if __name__ == "__main__":
    print(pokemon_attack_damage("fire -> grass"))
    print(pokemon_attack_damage("fighting -> ice rock"))
    print(pokemon_attack_damage("psychic -> poison dark"))
    print(pokemon_attack_damage("water -> normal"))
    print(pokemon_attack_damage("fire -> rock"))

"""
fire -> grass
fighting -> ice rock
psychic -> poison dark
water -> normal
fire -> rock
"""


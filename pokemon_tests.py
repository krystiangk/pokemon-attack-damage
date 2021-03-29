from unittest import TestCase
from pokemon import pokemon_attack_damage


class PokemonTests(TestCase):

    def test_pokemon_fire_grass(self):
        result = pokemon_attack_damage("fire -> grass")
        self.assertEqual(result, "2x")

    def test_pokemon_fighting_ice_rock(self):
        result =pokemon_attack_damage("fighting -> ice rock")
        self.assertEqual(result, "4x")

    def test_pokemon_psychic_poison_dark(self):
        result = pokemon_attack_damage("psychic -> poison dark")
        self.assertEqual(result, "0x")

    def test_pokemon_water_normal(self):
        result = pokemon_attack_damage("water -> normal")
        self.assertEqual(result, "0x")

    def test_pokemon_fire_rock(self):
        result = pokemon_attack_damage("fire -> rock")
        self.assertEqual(result, "0.5x")

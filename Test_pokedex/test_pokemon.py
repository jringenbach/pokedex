# coding: utf-8

from pokedex.pokemon import Pokemon

def test_is_same_pokemon_as():
    pokemon_to_test = Pokemon(1, "bulbasaur", "url_xxx")
    pokemon_to_test_2 = Pokemon(1, "bulbasaur", "url_xxx")
    those_previous_pokemon_are_the_same = pokemon_to_test.is_same_pokemon_as(pokemon_to_test_2)
    assert those_previous_pokemon_are_the_same == True
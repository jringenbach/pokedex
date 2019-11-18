# coding: utf-8

from pokedex.pokemon import Pokemon

def test_is_same_pokemon_as():
    #Pokemon object used for the test
    pokemon_to_test = Pokemon(1, "bulbasaur", "url_xxx")
    pokemon_to_test_2 = Pokemon(1, "bulbasaur", "url_xxx")
    pokemon_to_test_3 = Pokemon(2, "pokemon_two", "new_url")

    #Use of method is_same_pokemon_as(pokemon)
    those_previous_pokemon_are_the_same = pokemon_to_test.is_same_pokemon_as(pokemon_to_test_2)
    pokemon_are_not_the_same = pokemon_to_test_3.is_same_pokemon_as(pokemon_to_test)

    assert those_previous_pokemon_are_the_same == True
    assert pokemon_are_not_the_same == False
    
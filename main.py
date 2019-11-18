# coding: utf-8

from API.pokemonAPI import PokemonAPI

list_pokemon = PokemonAPI(params={"limit" : 100}).get_pokemon_from_api()
for pokemon in list_pokemon:
    pokemon.about_me()

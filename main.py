#!/usr/bin/python3
# coding: utf-8

#My own libraries
from API.pokemonAPI import PokemonAPI
from app import app

list_pokemon = PokemonAPI(params={"limit" : 5}).get_pokemon_from_api()
for pokemon in list_pokemon:
    pokemon.about_me()

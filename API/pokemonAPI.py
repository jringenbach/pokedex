#!/usr/bin/python3
# coding: utf-8


from pokedex.pokemon import Pokemon
import requests

class PokemonAPI:
    """Methods to GET Pokemon from the PokeAPI : https://pokeapi.co/api/v2/pokemon"""



    def __init__(self, url="https://pokeapi.co/api/v2/pokemon", params=None):
        self.url = url
        self.params = params



    def get_pokemon_from_api(self):
        """Return a list of Pokemon object by requesting the PokeAPI"""
        
        list_pokemon = list()

        #Get the list of all pokemons
        r = requests.get(self.url, params=self.params)
        r = r.json()

        for pokemon in r["results"]:

            #Request that gets information about this pokemon
            r_pokemon_id = requests.get(pokemon["url"])
            r_pokemon_id = r_pokemon_id.json()

            #Request that helps us get the sprite of this pokemon
            r_form = requests.get(r_pokemon_id["forms"][0]["url"])
            r_form = r_form.json()

            #We instanciate our pokemon information
            pokemon_name = pokemon["name"]
            pokemon_id = pokemon["url"].split("/")[6]
            pokemon_sprites = r_form["sprites"]["front_default"]

            list_pokemon.append(Pokemon(pokemon_id, pokemon_name, pokemon_sprites ))

        return list_pokemon
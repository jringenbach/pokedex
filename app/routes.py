#!/usr/bin/python3
# coding: utf-8

from flask import render_template
from API.pokemonAPI import PokemonAPI
from app import app

@app.route('/')
def index():
    """Index du site web"""

    return render_template("index.html", title="Accueil")



@app.route('/pokedex')
def pokedex():
    """Page affichant le pokédex"""

    list_pokemon = PokemonAPI(params={"limit" : 21}).get_pokemon_from_api()
    return render_template("pokedex.html", title="Pokédex", list_pokemon=list_pokemon)
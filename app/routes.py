#!/usr/bin/python3
# coding: utf-8

from flask import render_template
from API.pokemonAPI import PokemonAPI
from app import app

@app.route('/')
@app.route('/index')
def index():
    list_pokemon = PokemonAPI(params={"limit" : 5}).get_pokemon_from_api()
    return render_template("index.html", title="Pokédex", list_pokemon=list_pokemon)
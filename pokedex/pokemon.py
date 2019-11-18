class Pokemon:



    def __init__(self, pokeapi_id, name, sprites):
        """Initialization of a Pokemon Object
        
        id : integer that defines a unique Pokemon object
        name : string that defines the Pokemon name
        sprites : string containing the url where to find the sprite in png format"""
        self.id = pokeapi_id
        self.name = name
        self.sprites = sprites



    def about_me(self):
        """Print on the terminal the attributes of this pokemon"""

        print("id : "+str(self.id))
        print("name : "+self.name)
        print("sprite url : "+self.sprites)



    def is_same_pokemon_as(self, pokemon):
        """Test if two pokemon objects are the same. Return True if they are, False else.
        
        pokemon : a Pokemon Object"""

        if self.id == pokemon.id:
            return True
        else:
            return False
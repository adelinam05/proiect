from Pokemon import Pokemon

class Antrenor:
    def __init__(self,nume, pokemoni):
        self.nume = nume
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                return pokemon
            else:
                return None

    def are_pokemoni_vii(self):
        k = 0
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                k += 1
        if k > 0:
            return True
        else:
            return False
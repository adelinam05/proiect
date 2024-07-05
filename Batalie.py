from Antrenor import Antrenor

class Batalie:
    def lupta(self, antrenor1, antrenor2):
        while antrenor1.are_pokemoni_vii() and antrenor2.are_pokemoni_vii():
            pokemon1 = antrenor1.alege_pokemon()
            pokemon2 = antrenor2.alege_pokemon()
            if not pokemon1 or not pokemon2:
                break
            print(f"Lupta începe între {pokemon1.nume} și {pokemon2.nume}!")
            while pokemon1.este_viu() and pokemon2.este_viu():
                pokemon1.ataca(pokemon2)
                if pokemon2.este_viu():
                    pokemon2.ataca(pokemon1)
            if not pokemon1.este_viu():
                print(f"{pokemon1.nume} a pierdut!")
            if not pokemon2.este_viu():
                print(f"{pokemon2.nume} a pierdut!")
        if antrenor1.are_pokemoni_vii():
            print(f"Lupta a fost castigata de antrenorul {antrenor1.nume}!")
        else:
            print(f"Lupta a fost castigata de antrenorul {antrenor2.nume}!")
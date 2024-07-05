from Pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie

def input_pokemoni():
    pokemoni_antrenor1 = []
    pokemoni_antrenor2 = []
    print("Introducere Pokemoni pentru Antrenorul 1:")
    while True:
        nume = input("Introduceti numele Pokemonului sau 'stop' pentru a opri introducerea Pokemonilor pentru Antrenorul 1: ")
        if nume.lower() == "stop":
            break
        tip = input("Introduceti tipul Pokemonului (Foc/Apa/Pamant): ").lower()
        viata = int(input("Introduceti viața Pokemonului: "))
        putere_atac = int(input("Introduceti puterea de atac a Pokemonului: "))
        pokemon = Pokemon(nume, tip, viata, putere_atac)
        pokemoni_antrenor1.append(pokemon)

    print("Introducere Pokemoni pentru Antrenorul 2:")
    while True:
        nume = input("Introduceti numele Pokemonului sau 'stop' pentru a opri introducerea Pokemonilor pentru Antrenorul 2: ")
        if nume.lower() == "stop":
            break
        tip = input("Introduceti tipul Pokemonului (Foc/Apa/Pamant): ")
        viata = int(input("Introduceti viața Pokemonului: "))
        putere_atac = int(input("Introduceti puterea de atac a Pokemonului: "))
        pokemon = Pokemon(nume, tip, viata, putere_atac)
        pokemoni_antrenor2.append(pokemon)

    return pokemoni_antrenor1, pokemoni_antrenor2

pokemoni_antrenor1, pokemoni_antrenor2  = input_pokemoni()


antrenor1 = Antrenor("May", pokemoni_antrenor1)
antrenor2 = Antrenor("Iris", pokemoni_antrenor2)


batalie = Batalie()
batalie.lupta(antrenor1, antrenor2)


def starea_finala(antrenor):
    print(f"Antrenorul {antrenor.nume} are următorii Pokemoni:")
    for pokemon in antrenor.pokemoni:
        if pokemon.este_viu():
            pokemon.status = "viu"
        else:
            pokemon.status = "fara viata"
        print(f" Pokemonul: {pokemon.nume}, status: {pokemon.status} (viață rămasă: {pokemon.viata})")

starea_finala(antrenor1)
starea_finala(antrenor2)
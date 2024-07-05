class Pokemon:
    def __init__(self, nume, tip, viata, putere_atac):
        self.nume = nume
        self.tip = tip
        self.viata = viata
        self.putere_atac = putere_atac

    def ataca(self,alt_pokemon):
        if alt_pokemon.viata != 0 and self.viata != 0:
            alt_pokemon.viata -= self.putere_atac
        print(f"{self.nume} ataca pe {alt_pokemon.nume} si ii reduce viata la {alt_pokemon.viata}.")

    def este_viu(self):
        if self.viata>0:
            return True
        else:
            return False

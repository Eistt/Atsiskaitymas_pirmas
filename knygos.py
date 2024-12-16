from datetime import datetime


class Knygos:
    def __init__(self, pavadinimas, autorius, leidimo_metai, zanras, kiekis=1,grazinimo_data=None, terminas=None ):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.leidimo_metai = leidimo_metai
        self.zanras = zanras
        self.kiekis = kiekis
        self.terminas = terminas  
        self.grazinimo_data = grazinimo_data
    def knygos_info(self):
        return {
            "pavadinimas": self.pavadinimas,
            "autorius": self.autorius,
            "leidimo_metai": self.leidimo_metai,
            "zanras": self.zanras,
            "kiekis": self.kiekis
        }

    def yra_veluojanti(self):
        if self.grazinimo_data is not None and self.grazinimo_data < datetime.now():
            return True
        

    def __str__(self):
        return f"{self.pavadinimas} ({self.leidimo_metai}) autorius {self.autorius}"

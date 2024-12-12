class Knygos:
    def __init__(self, pavadinimas, autorius, leidimo_metai, zanras):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.leidimo_metai = leidimo_metai
        self.zanras = zanras
        self.kiekis = 0

    def knygos_info(self):
        return {
            "pavadinimas": self.pavadinimas,
            "autorius": self.autorius,
            "leidimo_metai": self.leidimo_metai,
            "zanras": self.zanras,
            "kiekis": self.kiekis
        }

    def __str__(self):
        return f" {self.pavadinimas} ({self.leidimo_metai}) autorius {self.autorius}  "

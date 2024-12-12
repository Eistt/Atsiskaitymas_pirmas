class Knygos:
    def __init__(self, pavadinimas, autorius, leidimo_metai, zanras, kiekis=1):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.leidimo_metai = leidimo_metai
        self.zanras = zanras
        self.kiekis = kiekis

    def knygos_info(self):
        return {
            "pavadinimas": self.pavadinimas,
            "autorius": self.autorius,
            "leidimo_metai": self.leidimo_metai,
            "zanras": self.zanras,
            "kopijos": self.kiekis
        }

    def __str__(self):
        return f"Knyga {self.pavadinimas} leidimo metai {self.leidimo_metai} autorius {self.autorius} zanras {self.zanras} ({self.kiekis} kopijos)"

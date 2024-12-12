from datetime import datetime, timedelta
from modeliai.knygos import Knygos


class Biblioteka:
    def __init__(self,failas):
        self.failas = failas
        self.knygos = []

    def prideti_knyga(self, knyga: Knygos):
        self.knygos.append(knyga)
        print(f"Knyga pridėta: {knyga}")
        
        
    def pasalinti_knyga(self, pavadinimas):
        self.knygos = list(filter(lambda knyga: knyga.pavadinimas != pavadinimas, self.knygos))
        self.issaugoti_biblioteka()
        print(f"Knyga pašalinta: {pavadinimas}")

    def paimti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas and knyga.kiekis > 0:
                knyga.kiekis -= 1
                grazinimo_data = datetime.now() + timedelta(days=30)
                print(f"Knyga '{pavadinimas}' paimta. Grazinimo terminas: {grazinimo_data.strftime('%Y-%m-%d')}")
                self.issaugoti_biblioteka()
                return
        print(f"Knygos '{pavadinimas}' neturime ")

    def grazinti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas:
                knyga.kopijos += 1
                print(f"Knyga '{pavadinimas}' grąžinta.")
                self.issaugoti_biblioteka()
                return
        print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

    def perziureti_knygas(self):
        if not self.knygos:
            print("Biblioteka tuščia.")
        else:
            for knyga in self.knygos:
                print(knyga)
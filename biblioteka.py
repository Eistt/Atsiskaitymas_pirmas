from datetime import datetime, timedelta
from knygos import Knygos


class Biblioteka:
    def __init__(self):
        self.knygos = []

    def prideti_knyga(self, knyga: Knygos):
        
        for esama_knyga in self.knygos:
            if esama_knyga.pavadinimas == knyga.pavadinimas:
                esama_knyga.kiekis +=1
                print(f"Knygos kiekis padidintas: {knyga}")
                return
            else:
             self.knygos.append(knyga)
            print(f"Knyga pridėta: {knyga}")
        
        
    def pasalinti_knyga(self, pavadinimas):
        self.knygos = list(filter(lambda knyga: knyga.pavadinimas == pavadinimas, self.knygos))
        self.knygos-=1
        print(f"Knyga pašalinta: {pavadinimas}")

    def paimti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas and knyga.kiekis > 0:
                knyga.kiekis -= 1
                grazinimo_data = datetime.now() + timedelta(days=30)
                print(f"Knyga '{pavadinimas}' paimta. Grazinimo terminas yra: {grazinimo_data.strftime('%Y-%m-%d')}")
                return
            else:
                print(f"Knygos '{pavadinimas}' neturime ")

    def grazinti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas:
                knyga.kiekis += 1
                print(f"Knyga '{pavadinimas}' grąžinta.")
                
                return
        print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

    def perziureti_knygas(self):
        if not self.knygos:
            print("Biblioteka tuščia.")
        else:
            print(self.knygos)
            # for knyga in self.knygos:
            #     print(f" {knyga.pavadinimas}, {knyga.autorius}, {knyga.metai} {knyga.zanras}, {knyga.kiekis}")

    
    def issaugoti_biblioteka(self):
        pass


# biblioteka = Biblioteka()
# knyga1 = Knygos("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 3)
# knyga2 = Knygos("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 2)

# biblioteka.prideti_knyga(knyga1)
# biblioteka.prideti_knyga(knyga2)

# # Patikriname bibliotekoje esančias knygas
# biblioteka.perziureti_knygas()

# # Paimame knygą
# biblioteka.paimti_knyga("Harry Potter")
# biblioteka.perziureti_knygas()

# # Grąžiname knygą
# biblioteka.grazinti_knyga("Harry Potter")
# biblioteka.perziureti_knygas()



from datetime import datetime, timedelta
from knygos import Knygos
import pickle

class Biblioteka:
    def __init__(self, failas="biblioteka.pkl"):
        self.knygos = []
        self.failas=failas
        self.pateikti_knygas()  
        

    def prideti_knyga(self, knyga: Knygos):
     for esama_knyga in self.knygos:
        if esama_knyga.pavadinimas.lower() == knyga.pavadinimas.lower():
            esama_knyga.kiekis += 1
            print(f"Knyga prideta: {knyga.pavadinimas}")
            return
     self.knygos.append(knyga)
     print(f"Knyga pridėta: {knyga.pavadinimas}")
     self.issaugoti_biblioteka()
        

    def pasalinti_knyga(self, pavadinimas):
        self.knygos = list(filter(lambda knyga: knyga.pavadinimas.lower() !=pavadinimas.lower(), self.knygos))
        print(f"Knyga pašalinta: {pavadinimas}")
        self.issaugoti_biblioteka()


    def paimti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower() and knyga.kiekis > 0:
                knyga.kiekis -= 1
                knyga.grazinimo_data = datetime.now() + timedelta(days=30)
                print(f"Knyga '{pavadinimas}' paimta. Grazinimo terminas yra: {knyga.grazinimo_data.strftime('%Y-%m-%d')}")
            else:
                print(f"Knygos '{pavadinimas}' neturime ")


    def grazinti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower():
                knyga.kiekis += 1
                print("Visos knygos ir jų grąžinimo datos:")
                for knyga in self.knygos:
                    print(knyga.pavadinimas, knyga.grazinimo_data)
                return
        print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")


    def perziureti_knygas(self):
        if not self.knygos:
            print("Biblioteka tuscia.")
        else:
            print("Knygu sarasas")
            for knyga in self.knygos:
                print(f" {knyga.pavadinimas}, {knyga.autorius}, {knyga.leidimo_metai} {knyga.zanras}, {knyga.kiekis}")
    
    def perziureti_veluojancias(self):
        dabar = datetime.now()
        veluojancios = filter(lambda knyga: knyga.grazinimo_data and knyga.grazinimo_data < dabar,self.knygos)
        veluojancios = list(veluojancios)
        if not veluojancios:
            print("Nėra vėluojančių knygų.")
        else:
            for knyga in veluojancios:
                veluojamos_dienos = (dabar - knyga.grazinimo_data).days
                print(f"{knyga.pavadinimas}, grąžinimo terminas buvo: {knyga.grazinimo_data.strftime('%Y-%m-%d')}, vėluojama: {veluojamos_dienos} dienas")

    
    def ieskoti_knygos(self, vartotojo_ivestis, reiksme ):
        
        rezultatai=self.knygos
         
        if  vartotojo_ivestis== "pavadinimas":
            rezultatai = filter(lambda knyga: reiksme.lower() in knyga.pavadinimas.lower(), rezultatai)
        elif  vartotojo_ivestis== "autorius":
            rezultatai = filter(lambda knyga: reiksme.lower() in knyga.autorius.lower(), rezultatai)
        elif  vartotojo_ivestis== "zanras":
            rezultatai = filter(lambda knyga: reiksme.lower() in knyga.zanras.lower(), rezultatai)
        elif vartotojo_ivestis == "metai":
          try:
               metai = int(reiksme)
               rezultatai = filter(lambda knyga: knyga.leidimo_metai == metai, rezultatai)
          except ValueError:
            print("Įvestas neteisingas metų formatas.")
            return
        
        rezultatai = list(rezultatai)
        if rezultatai:
            print(f"Rastos knygos: {vartotojo_ivestis}")
            for knyga in rezultatai:
                print(f"{knyga.pavadinimas}, {knyga.autorius}, {knyga.zanras}, {knyga.kiekis} vnt.")
        else:
            print("Nėra knygų pagal šiuos kriterijus.")



    # def perziureti_veluojancias(self):
    #     dabar= datetime.now()
    #     veluojancios= filter(lambda knyga: knyga.grazinimo_data and knyga.grazinimo_data < dabar,self.knygos)
    #     veluojancios= list(veluojancios)
    #     if not veluojancios:
    #         print("Nera veluojanciu knygu")
    #     else:
    #         for knyga in veluojancios:
    #             veluojamos_dienos= (dabar-knyga.grazinimo_data).days
    #             print(f"{knyga.pavadinimas}, grazinimo terminas buvo: {knyga.grazinimo_data.strftime('%Y-%m-%d')}, vėluojama: {veluojamos_dienos} dienas")
        
                
    def issaugoti_biblioteka(self):
        with open(self.failas, 'wb') as f:
            pickle.dump(self.knygos, f)
            
            
    def pateikti_knygas(self):
        try:
            with open(self.failas, 'rb') as f:
                self.knygos = pickle.load(f)
            # Patikrinkite kiekvieną knygą
            for knyga in self.knygos:
                if not hasattr(knyga, 'grazinimo_data'):
                    knyga.grazinimo_data = None
        except FileNotFoundError:
            print("Nerasta anksčiau saugotų knygų. Biblioteka bus tuščia.")

# def pateikti_knygas(self):
#     with open(self.failas, 'rb') as f:
#             pickle.load(self.knygos, f)



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



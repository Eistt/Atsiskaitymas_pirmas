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
     print(f"Knyga prideta: {knyga.pavadinimas}")
     self.issaugoti_biblioteka()
        

    def pasalinti_knyga(self, pavadinimas):
        self.knygos = list(filter(lambda knyga: knyga.pavadinimas.lower() !=pavadinimas.lower(), self.knygos))
        print(f"Knyga pasalinta: {pavadinimas}")
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
            if knyga.pavadinimas == pavadinimas:
                knyga.kiekis += 1
                knyga.grazinimo_data = None  
                print(f"Knyga '{pavadinimas}' grąžinta.")
                return
        print("Knyga nerasta.")


    def perziureti_knygas(self):
        if not self.knygos:
            print("Biblioteka tuscia")
        else:
            print("Knygu sarasas")
            for knyga in self.knygos:
                print(f"Knyga: {knyga.pavadinimas}, {knyga.autorius}({knyga.leidimo_metai}),Zanras [{knyga.zanras}], {knyga.kiekis}vnt")
    
    def perziureti_veluojancias(self):
        dabar = datetime.now()
        veluojancios = filter(lambda knyga: knyga.grazinimo_data and knyga.grazinimo_data < dabar,self.knygos)
        veluojancios = list(veluojancios)
        if not veluojancios:
            print("Nėra vėluojančių knygų.")
        else:
            for knyga in veluojancios:
                veluojamos_dienos = (dabar - knyga.grazinimo_data).days
            print(f"{knyga.pavadinimas}, grąžinimo terminas buvo buvo: {knyga.grazinimo_data.strftime('%Y-%m-%d')}, vėluojama: {veluojamos_dienos} dienas")
    
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

                
    def issaugoti_biblioteka(self):
        with open(self.failas, 'wb') as f:
            pickle.dump(self.knygos, f)
            
            
    def pateikti_knygas(self):
        try:
            with open(self.failas, 'rb') as f:
                self.knygos = pickle.load(f)
            for knyga in self.knygos:
                if not hasattr(knyga, 'grazinimo_data'):
                    knyga.kiekis=1
        except FileNotFoundError:
            print("biblioteka tuscia")





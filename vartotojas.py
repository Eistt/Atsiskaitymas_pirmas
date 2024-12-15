import random
import pickle
import datetime


class Vartotojas:
    def __init__(self):
        self.vardas = ""
        self.pavarde = ""
        self.id_numeris = ""
        self.paimtos_knygos = [] 

    def generuotojas(self):
        vardas_initials = self.vardas[:2].upper()
        pavarde_initials = self.pavarde[:2].upper()
        random_numeris = random.randint(100000, 999999)
        self.id_numeris = f"{vardas_initials}{pavarde_initials}{random_numeris}"

    def __str__(self):
        return f"Vartotojo vardas: {self.vardas}, pavardė: {self.pavarde}, ID numeris: {self.id_numeris}"

    def rasti_ieskoti(self, vardas, pavarde, vartotoju_sarasas):
        for user in vartotoju_sarasas:
            if user.vardas.lower() == vardas.lower() and user.pavarde.lower() == pavarde.lower():
                return user
        

    def rasti_ieskoti_id(self, id_numeris, vartotoju_sarasas):
        for user in vartotoju_sarasas:
            if user.id_numeris == id_numeris:
                return user
      

    def naujas_user(self, vardas, pavarde, vartotoju_sarasas):
        new_user = Vartotojas()
        new_user.vardas = vardas
        new_user.pavarde = pavarde
        new_user.generuotojas()
        vartotoju_sarasas.append(new_user)
        return new_user
    
    def yra_veluojanti(self):
        if self.grazinimo_data and self.grazinimo_data < datetime.now():
            return True
        # dabar = datetime.datetime.now()
        # for knyga_info in self.paimtos_knygos:
        #     if knyga_info["grazinimo_data"] < dabar:
        #         return True
        # return False
    
    def paimti_knyga(self, knyga):
        self.paimtos_knygos.append(knyga)
        print(f"Knyga '{knyga.pavadinimas}' paimta. Grazinimo data: {knyga.grazinimo_data}")

    def grazinti_knyga(self, knyga):
        if knyga in self.paimtos_knygos:
            self.paimtos_knygos.remove(knyga)
            knyga.grazinimo_data = None
            print(f"Knyga '{knyga.pavadinimas}' grąžinta.")
        else:
            print(f"Knyga '{knyga.pavadinimas}' nebuvo paimta.")
    


    def issaugoti_vartotojus(self, vartotoju_sarasas):
        with open('vartotojai.pkl', 'wb') as f:
            pickle.dump(vartotoju_sarasas, f)
        print("Vartotojai išsaugoti sėkmingai.")

    def nuskaityti_vartotojus(self):
        try:
            with open('vartotojai.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Failas nerastas, kuriamas naujas sąrašas.")
            return []
        


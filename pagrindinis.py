from modeliai.biblioteka import Biblioteka
from modeliai.knygos import Knygos

def pagrindinis():
    biblioteka= Biblioteka()
    
    biblioteka.knygos= biblioteka.nuskaityti_biblioteka()




    while True:
        print("***************SVEIKI ATVYKE I VIRTUALIA BIBLIOTEKA*************** \n\n Pasirinkite koki veiksma noresite atlikti ")
        veiksmai= input(" 1. Prideti knyga\n 2. Pasalinti knyga\n 3. Pasiimti knyga\n 4. Grazinti knyga\n 5. Perziureti esančias knygas bibliotekoje\n 6. Perziureti visas veluojancias knygas \n 7. Iseiti is bibliotekos\n")

        if  veiksmai == "1":
            pavadinimas= input(" Iveskite pavadinima: ")
            autorius= input ("Iveskite autoriu: ")
        
           
            while True:
                try:
                    leidimo_metai= int(input ("Iveskite leidimo metus tarp 1800-2024: "))
                    if leidimo_metai<=2024 and leidimo_metai>=1800:
                        print("Ivesti metai negalimi")
                        break
                except ValueError:
                    print("Iveskite metus skaiciais")
                    continue
                    
                zanras= input("Iveskite knygos zanra ")
                prideta_knyga= Knygos(pavadinimas, autorius, leidimo_metai,zanras)
                biblioteka.prideti_knyga(prideta_knyga)
                
            
        if veiksmai=="2":
            try:
                metai= int(input("Iveskite metus iki kuriu pasalinti knygas: "))
                if metai>2024 or metai<1800:
                    print("Tokie metai negalimi, veskite dar karta ")
                else:
                    biblioteka.knygos = list(filter(lambda knyga: knyga.leidimo_metai > metai, biblioteka.knygos))
                    biblioteka.issaugoti_biblioteka()
            except ValueError:
                print(" Ivedete ne metus, bandykite dar karta")
                continue
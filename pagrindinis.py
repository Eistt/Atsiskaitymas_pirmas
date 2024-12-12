from biblioteka import Biblioteka
from knygos import Knygos

def pagrindinis():
    biblioteka= Biblioteka()
    
   
    print("\n***************SVEIKI ATVYKE I VIRTUALIA BIBLIOTEKA*************** \n\n Pasirinkite koki veiksma noresite atlikti ")
    while True:
        
        veiksmai= input("\n 1. Prideti knyga\n 2. Pasalinti knyga\n 3. Pasiimti knyga\n 4. Grazinti knyga\n 5. Perziureti esančias knygas bibliotekoje\n 6. Perziureti visas veluojancias knygas \n 7. Iseiti is bibliotekos\n")

        if  veiksmai == "1":
            pavadinimas= input(" Iveskite pavadinima: ")
            autorius= input ("Iveskite autoriu: ")
            
            while True:
                try:
                    leidimo_metai = int(input("Iveskite leidimo metus tarp 1800-2024: "))
                    
                    if leidimo_metai < 1800 or leidimo_metai > 2024:
                        print("Ivesti metai negalimi, bandykite dar karta. Metai turi būti tarp 1800 ir 2024.")
                        continue
                    
                except ValueError:
                    print("Iveskite metus skaiciais")
                    continue
                    
                zanras= input("Iveskite knygos zanra ")
                prideta_knyga= Knygos(pavadinimas, autorius, leidimo_metai,zanras)
                biblioteka.prideti_knyga(prideta_knyga)
                print(f" Jus sekmingai pridejote knyga ")
                break
            
        if veiksmai=="2":
            
            while True:
                try:
                    metai= int(input("Iveskite metus iki kuriu pasalinti knygas: "))
                    if metai>2024 or metai<1800:
                     print("Tokie metai negalimi, veskite dar karta ")
                     
                    else:
                     biblioteka.knygos = list(filter(lambda knyga: knyga.leidimo_metai > metai, biblioteka.knygos))
                     biblioteka.issaugoti_biblioteka()
                     print(f"Jus sekmingai pasalinote knygas iki {metai} metu ")
                     break
                except ValueError:
                    print(" Iveskite metus skaiciais")
                    
            
        elif veiksmai=="3":
            kokia_knyga_pasiimti= input("Iveskite knygos pavadinima, kuria norite pasiimti ")
            biblioteka.paimti_knyga(kokia_knyga_pasiimti)

        elif veiksmai=="4":
           sugrazinti_knyga= input("Iveskite knygos pavadinima, kuria norite grazinti ")
           biblioteka.grazinti_knyga(sugrazinti_knyga)
    
        elif veiksmai=="5":
           print("Bibliotekoje esanciu knygu sarasas: ")
           biblioteka.perziureti_knygas()

        # # elif veiksmai=="6":
        # #    print("Veluojanciu grazinti knygu sarasas: ")

        
        # elif veiksmai=="7":
        #    print("Aciu, jog lankotes musu bibliotekoje\nGeros dienos ")
        #    break

pagrindinis()





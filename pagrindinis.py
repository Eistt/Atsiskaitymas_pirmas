from biblioteka import Biblioteka
from knygos import Knygos
from vartotojas import Vartotojas

biblioteka= Biblioteka()


def pagrindinis():
    vartotoju_paieska = Vartotojas()
    vartotoju_sarasas = vartotoju_paieska.nuskaityti_vartotojus()
    if True:
      
            pasirinkimas = input("Pasirinkite, ką norite įvesti (1 - Varda ir pavarde, 2 - ID numeri): ").strip()
            vartotoju_paieska = Vartotojas()
    if pasirinkimas == "1":
        vardas = input("Įveskite vartotojo vardą: ").strip()
        pavarde = input("Įveskite vartotojo pavardę: ").strip()
        esamas_vartotojas = vartotoju_paieska.rasti_ieskoti(vardas, pavarde, vartotoju_sarasas)
    elif pasirinkimas == "2":
        id_numeris = input("Įveskite vartotojo ID numerį: ").strip()
        esamas_vartotojas = vartotoju_paieska.rasti_ieskoti_id(id_numeris, vartotoju_sarasas)
    else:
        print("Neteisingas pasirinkimas")
    if esamas_vartotojas:
        print(f"Sveiki sugrįžę {esamas_vartotojas}")
    elif not esamas_vartotojas:
        print("Sekmingai sukureme jums paskyra")
  

    vartotoju_paieska.issaugoti_vartotojus(vartotoju_sarasas)


    while True:
        
        veiksmai = input("\n 1. Pridėti knygą\n 2. Pašalinti knygą\n 3. Pasiimti knygą\n 4. Grąžinti knygą\n 5. Peržiūrėti esančias knygas bibliotekoje\n 6. Peržiūrėti visas vėluojančias knygas\n 7. Ieškoti knygos\n 8. Išeiti iš bibliotekos\n ")

        if veiksmai == "1":
            pavadinimas = input("Iveskite pavadinima: ").strip()
            autorius = input("Iveskite autoriu: ").strip()
            while True:
                try:
                    leidimo_metai = int(input("Įveskite leidimo metus tarp 1800-2024: "))
                    if leidimo_metai < 1800 or leidimo_metai > 2024:
                        print("Įvesti metai negalimi, bandykite dar kartą. Metai turi būti tarp 1800 ir 2024.")
                        continue
                except ValueError:
                    print("Įveskite metus skaičiais")
                    continue
                zanras = input("Įveskite knygos žanrą: ")
                prideta_knyga = Knygos(pavadinimas, autorius, leidimo_metai, zanras)
                biblioteka.prideti_knyga(prideta_knyga)
                print("Jūs sėkmingai pridėjote knygą.")
                break
            
        elif veiksmai == "2":
            while True:
                try:
                    metai = int(input("Įveskite metus, iki kurių pašalinti knygas: "))
                    if metai > 2024 or metai < 1800:
                        print("Tokie metai negalimi, veskite dar kartą.")
                    else:
                        biblioteka.knygos = list(filter(lambda knyga: knyga.leidimo_metai > metai, biblioteka.knygos))
                        biblioteka.issaugoti_biblioteka()
                        print(f"Jūs sėkmingai pašalinote knygas iki {metai} metų.")
                        break  
                except ValueError:
                    print("Įveskite metus skaičiais")
            
        elif veiksmai == "3":
                if esamas_vartotojas is not None:
                    if esamas_vartotojas.yra_veluojanti():
                     print(f"{esamas_vartotojas.vardas} turit veluojaciu knygu ")
                else:
                    kokia_knyga_pasiimti = input("Įveskite knygos pavadinima, kuri norite pasiimti: ")
                    for knyga in biblioteka.knygos:
                        if knyga.pavadinimas.lower() == kokia_knyga_pasiimti.lower() and knyga.kiekis >0:
                            esamas_vartotojas.paimti_knyga(knyga)
                            biblioteka.paimti_knyga(kokia_knyga_pasiimti) 
                            break
                    else:
                        print("Knyga nerasta bibliotekoje.")

        elif veiksmai == "4":
            try:
                  if not esamas_vartotojas:
                      print("Jus neturite ko grazinti")
                      continue
                  if esamas_vartotojas:
                      sugrazinti_knyga = input("Įveskite knygos pavadinimą, kurią norite grazinti: ")
                      for knyga in esamas_vartotojas.paimti_knyga:
                          if knyga.pavadinimas.lower() == sugrazinti_knyga.lower():
                              esamas_vartotojas.grazinti_knyga(knyga)
                              biblioteka.grazinti_knyga(sugrazinti_knyga)
                              break
            except TypeError: 
                print("ivedete blogai")

        elif veiksmai == "5":
            print("Bibliotekoje esanciu knygu sąrasas: ")
            biblioteka.perziureti_knygas()

        elif veiksmai == "6":
            print("Bibliotekoje veluojanciu knygu sarasas: ")
            biblioteka.perziureti_veluojancias()

        elif veiksmai == "7":
            ivestis = input("Įveskite, kokios knygos norite ieskoti (autorius/zanras/pavadinimas): ")
            ivestis2 = input("Įveskite duomenis: ").strip()
            print("Knyga pagal jūsų paieška: ")
            biblioteka.ieskoti_knygos(ivestis, ivestis2)

        elif veiksmai == "8":
            print("Ačiū, jog lankotes bibliotekoje. Geros dienos!")
            break
pagrindinis()





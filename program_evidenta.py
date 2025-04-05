import modul                                                    #importam functille 

angajati = [

{'Nume': 'Akexandru', 'Prenume': 'Marius', 'CNP': '1910301471344', 'Varsta': 32, 'Salariu': 5000, 'Departament': 'Amazon', 'Senioritate': 'junior'},
{'Nume': 'Alexandru', 'Prenume': 'Daniel', 'CNP': '1910301471345', 'Varsta': 30, 'Salariu': 6000, 'Departament': 'Electrice', 'Senioritate': 'mid'},
{'Nume': 'Bustea', 'Prenume': 'Aurel', 'CNP': '1910301471346', 'Varsta': 33, 'Salariu': 7000, 'Departament': 'Frizerie', 'Senioritate': 'junior'},
{'Nume': 'Micu', 'Prenume': 'Marian', 'CNP': '1910301471344', 'Varsta': 31, 'Salariu': 9000, 'Departament': 'Frizerie', 'Senioritate': 'senior'}

]                                                   # adaugam lista cu angajati

while True:                                                     # ne asiguram ca meniul va fi intodeauna pe ecran
    print("\nMeniu")
    print("1. Adaugare angajat")
    print("2. Cautare angajat")
    print("3. Modificare angajat")
    print("4. Stergere angajat")
    print("5. Afisare angajati")
    print("6. Cost total salarii")
    print("7. Cost salarii pe departament")
    print("8. Fluturas de salariu")
    print("9. Afisare dupa senioritate")
    print("10. Afisare dupa departament")
    print("11. Iesire")

    optiune = input("Alegeti o optiune: ")



#apelam functiile in functie de numarul introdus, iar la sfarsit avem un break ca sa iesim din program si un else in caz ca nu introducem corect optiunea

    if optiune == "1":
        angajat = modul.adaugare_angajat()
        angajati.append(angajat)
    elif optiune == "2":
        modul.cautare_angajat(angajati)
    elif optiune == "3":
        modul.modificare_angajat(angajati)
    elif optiune == "4":
        modul.stergere_angajat(angajati)
    elif optiune == "5":
        modul.afisare_angajati(angajati)
    elif optiune == "6":
        modul.calcul_total_salariu(angajati)
    elif optiune == "7":
        modul.calcul_total_salariu_departament(angajati)
    elif optiune == "8":
        modul.fluturas_salariu(angajati)
    elif optiune == "9":
        modul.afisare_dupa_senioritate(angajati)
    elif optiune == "10":
        modul.afisare_dupa_departament(angajati)
    elif optiune == "11":
        print("Program incheiat.")
        break
    else:
        print("Optiune invalida. Incercati din nou.")


def adaugare_angajat():
    nume_angajat = input("Introduceti numele angajatului: ").capitalize()
    prenume_angajat = input("Introduceti prenumele angajatului: ").capitalize()

    while True:
        try:
            cnp = input("Introduceti CNP-ul angajatului: ")
            if not cnp.isdigit() or len(cnp) != 13:                               #aici am pus sa ma asigur ca cnp-ul este din numere si sa aiba exact lungimea de 13 numere
                raise ValueError("CNP-ul trebuie sa contina exact 13 cifre!")
            break
        except ValueError as e:
            print("Eroare:", e)

    while True:
        try:
            varsta = int(input("Introduceti varsta angajatului: "))
            if varsta < 18 or varsta > 65:                                        # m-am asigurat ca angajatul sa nu fie minor, dar nici pensionar
                raise ValueError("Varsta trebuie sa fie intre 18 si 65 de ani!")
            break
        except ValueError as e:
            print("Eroare:", e)

    while True:
        try:
            salariu = int(input("Introduceti salariul angajatului: "))
            if salariu < 4050:                                                    #Salariu minim brut este 4050 lei
                raise ValueError("Salariul minim brut este 4050!")
            break
        except ValueError as e:
            print("Eroare:", e)

    while True:
        try:
            departament = input("Introduceti numele departamentului: ").capitalize()
            if departament.isdigit():                                              # m-am gandit ca numele poate sa fie oricare, dar sa nu fie facut din numere     
                raise ValueError("Departamentul nu trebuie sa contina cifre!")
            break
        except ValueError as e:
            print("Eroare:", e)

    while True:
        try:
            senioritate = input("Introduceti senioritatea angajatului (junior, mid, senior): ").lower()
            if senioritate not in ["junior", "mid", "senior"]:                                           #utilizatorii sa foloseasca exact optiunile
                raise ValueError("Senioritatea trebuie sa fie: junior, mid sau senior")
            break
        except ValueError as e:
            print("Eroare:", e)

    return {
        "Nume": nume_angajat,
        "Prenume": prenume_angajat,
        "CNP": cnp,
        "Varsta": varsta,
        "Salariu": salariu,
        "Departament": departament,
        "Senioritate": senioritate
    }

def cautare_angajat(angajati):
    cnp = input("Introduceti CNP-ul angajatului pentru cautare: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:                                  #daca cheia se potriveste cu introducem noi pentru variablia cnp, atunci ne afiseaza dictionarul in cauza
            print("Angajat gasit:", angajat)
            return angajat
    print("Angajatul nu a fost gasit.")
    return None


#la modificare angajati am decis sa schimb doar varsta, salariu, departament si senioritate pentru ca numele sau cnp-ul ti-l modifici la primarie(logica mea :) ) 
# am adaugat un loop while pentru fiecare si erorile iar pentru ca daca greseam ceva ma punea sa le bag iar pe fiecare in parte



def modificare_angajat(angajati):
    cnp = input("Introduceti CNP-ul angajatului pentru modificare: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            while True:
                try:
                    varsta = int(input("Noua varsta: "))
                    if varsta < 18 or varsta > 65:
                        raise ValueError("Varsta invalida")
                    angajat["Varsta"] = varsta
                    break
                except ValueError as e:
                    print("Eroare:", e)
            while True:
                try:
                    salariu = int(input("Noul salariu: "))
                    if salariu < 4050:
                        raise ValueError("Salariu prea mic")
                    angajat["Salariu"] = salariu
                    break
                except ValueError as e:
                    print("Eroare:", e)
            while True:
                try:
                    departament = input("Noul departament: ").capitalize()
                    if departament.isdigit():
                        raise ValueError("Departament invalid")
                    angajat["Departament"] = departament
                    break
                except ValueError as e:
                    print("Eroare:", e)
            while True:
                try:
                    senioritate = input("Noua senioritate: ").lower()
                    if senioritate not in ["junior", "mid", "senior"]:
                        raise ValueError("Senioritate invalida")
                    angajat["Senioritate"] = senioritate
                    break
                except ValueError as e:
                    print("Eroare:", e)
            print("Datele au fost modificate cu succes!")
            return
    print("Angajatul nu a fost gasit.")

def stergere_angajat(angajati):
    cnp = input("Introduceti CNP-ul angajatului de sters: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            angajati.remove(angajat)                             #am folosit functia remove pentru liste
            print("Angajat sters cu succes!")
            return
    print("Angajatul nu a fost gasit.")

def afisare_angajati(angajati):
    if not angajati:                                            #in caz ca nu exista nimic in lista
        print("Nu exista angajati inregistrati.")             
    for angajat in angajati:                                    #asta fost cea mai simpla :)))
        print(angajat)

def calcul_total_salariu(angajati):
    total = 0
    for angajat in angajati:
        total += angajat["Salariu"]
    print("Cost total salarii:", total)

def calcul_total_salariu_departament(angajati):
    departament = input("Introduceti numele departamentului: ").capitalize()
    total = 0                                                                   #ii dam o valoare totalului
    for angajat in angajati:
        if angajat["Departament"] == departament:
            total += angajat["Salariu"]                                         #calculam salariu in functie de cheia departament
    print("Cost total pentru departamentul", departament + ":", total)

def fluturas_salariu(angajati):
    cnp = input("Introduceti CNP-ul angajatului: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            brut = angajat["Salariu"]                                           # adaugam valoarea salariului
            cas = 0.10 * brut                                                   # calculam procentajul din salariul brut pentru cas, cass
            cass = 0.25 * brut
            impozit = 0.10 * (brut - cas - cass)                                # scadem rezultatul din cas si cass si calculam iar procentajul
            net = brut - cas - cass - impozit                                   # calculam netul si ne rugam la Dumnezeu :)))
            print("Fluturas salariu pentru", angajat['Nume'], angajat['Prenume'] + ":")
            print("Brut:", brut, "CAS:", cas, "CASS:", cass, "Impozit:", impozit, "Net:", net)
            return
    print("Angajatul nu a fost gasit.")

def afisare_dupa_senioritate(angajati):
    for nivel in ["junior", "mid", "senior"]:                                   #luam valoarea nivelui si pentru fiecare nivel afisam angajatii corespondenti
        for angajat in angajati:
            if angajat["Senioritate"] == nivel:
                print(angajat)

def afisare_dupa_departament(angajati):
    departamente = []                                                   #am facut o lista departamente si adaugam valorile, iar dupa folosesc functia sorted pentru a sorta lista
    for angajat in angajati:
        if angajat["Departament"] not in departamente:
            departamente.append(angajat["Departament"])
    for dept in sorted(departamente):
        for angajat in angajati:
            if angajat["Departament"] == dept:
                print(angajat)

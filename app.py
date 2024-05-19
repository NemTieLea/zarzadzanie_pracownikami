class Manager:
    def __init__(self, imie_nazwisko, nazwa_dzialu, pensja):
        self.imie_nazwisko = imie_nazwisko
        self.nazwa_dzialu = nazwa_dzialu
        self.pensja = pensja

    def __str__(self):
        return f"<Manager: {self.nazwa_dzialu} [{self.imie_nazwisko}]>"


class Pracownik:
    def __init__(self, imie_nazwisko, nazwa_dzialu, stanowisko, pensja):
        self.imie_nazwisko = imie_nazwisko
        self.nazwa_dzialu = nazwa_dzialu
        self.stanowisko = stanowisko
        self.pensja = pensja

    def __str__(self):
        return f"<Pracownik: {self.imie_nazwisko} [{self.stanowisko}] w {self.nazwa_dzialu} >"


class CzlonekZarzadu:
    def __init__(self, imie_nazwisko, lista_dzialow, pensja):
        self.imie_nazwisko = imie_nazwisko
        self.lista_dzialow = lista_dzialow
        self.pensja = pensja

    def __str__(self):
        return f"<Zarzad: {self.imie_nazwisko} [nadzoruje: {self.lista_dzialow}]<"


def wczytaj_managera():
    imie_nazwisko = input('imie i nazwisko: ')
    dzial = input('dzial: ')
    pensja = float(input('pensja: '))
    nowy_manager = Manager(
        imie_nazwisko=imie_nazwisko,
        nazwa_dzialu=dzial,
        pensja=pensja
    )
    return nowy_manager


def wczytaj_pracownika():
    imie_nazwisko = input('imie i nazwisko: ')
    dzial = input('dzial: ')
    stanowisko = input('stanowisko: ')
    pensja = float(input('pensja: '))
    nowy_pracownik = Pracownik(
        imie_nazwisko=imie_nazwisko,
        nazwa_dzialu=dzial,
        stanowisko=stanowisko,
        pensja=pensja,
    )
    return nowy_pracownik


def wczytaj_czlonka_zarzadu():
    imie_nazwisko = input("imie i nazwisko: ")
    lista_dzialow = []
    while True:
        dzial = input("nazwa dzialu, puste aby przerwac: ")
        if not dzial:
            break
        lista_dzialow.append(dzial)
    pensja = input("pensja: ")
    nowy_czlonek_zarzadu = CzlonekZarzadu(
        imie_nazwisko=imie_nazwisko,
        lista_dzialow=lista_dzialow,
        pensja=pensja,
    )
    return nowy_czlonek_zarzadu


def wykonaj_akcje_podwladni(managerowie, pracownicy):
    manager_name = input('imie nazwisko managera: ')
    for m in managerowie:
        if m.imie_nazwisko == manager_name:
            print(m)
            for p in pracownicy:
                if p.nazwa_dzialu == m.nazwa_dzialu:
                    print(p)


def wykonaj_akcje_stanowisko(pracownicy):
    nazwa_stanowiska = input('nazwa stanowiska: ')
    for p in pracownicy:
        if p.stanowisko == nazwa_stanowiska:
            print(p)


def wykonaj_akcje_bilans(managerowie, pracownicy, zarzad):
    suma_pensji = 0
    for m in managerowie:
        suma_pensji += m.pensja
    for p in pracownicy:
        suma_pensji += p.pensja
    for cz in zarzad:
        suma_pensji += cz.pensja
    print(f"Suma pensji to: {suma_pensji}")


def wykonaj_akcje_czlonek_zarzadu(zarzad, managerowie):
    zarzad_name = input('imie nazwisko: ')
    for cz in zarzad:
        if cz.imie_nazwisko == zarzad_name:
            for m in managerowie:
                if m.nazwa_dzialu in cz.lista_dzialow:
                    print(m)


managerowie = []
pracownicy = []
zarzad = []


while True:
    akcja = input('utworz / zarzadzaj / koniec: ')
    if akcja == 'koniec':
        print("Koncze")
        break
    elif akcja == 'utworz':
        while True:
            akcja_wewnetrzna = input('manager / pracownik / czlonek zarzadu / koniec')
            if akcja_wewnetrzna == 'koniec':
                break
            elif akcja_wewnetrzna == 'czlonek zarzadu':
                nowy_czlonek_zarzadu = wczytaj_czlonka_zarzadu()
                zarzad.append(nowy_czlonek_zarzadu)
            elif akcja_wewnetrzna == 'manager':
                # Dodawanie nowego managera
                nowy_manager = wczytaj_managera()
                managerowie.append(nowy_manager)
            elif akcja_wewnetrzna == 'pracownik':
                # Dodawanie nowego pracownika
                nowy_pracownik = wczytaj_pracownika()
                pracownicy.append(nowy_pracownik)
            else:
                print("nie ma takiego stanowiska.")
    elif akcja == 'zarzadzaj:':
        while True:
            akcja_wewnetrzna = input('stanowisko / podwladni / czlonek zarzadu / bilans / koniec')
            if akcja_wewnetrzna == 'koniec':
                break
            elif akcja_wewnetrzna == 'czlonek zarzadu':
                wykonaj_akcje_czlonek_zarzadu(zarzad, managerowie)
            elif akcja_wewnetrzna == 'stanowisko':
                wykonaj_akcje_stanowisko(pracownicy)
            elif akcja_wewnetrzna == 'podwladni':
                wykonaj_akcje_podwladni(managerowie, pracownicy)
            elif akcja_wewnetrzna == 'bilans':
                wykonaj_akcje_bilans(managerowie, pracownicy, zarzad)
            else:
                print("nie ma takiej komendy")
    else:
        print("Nie ma takiej komendy...")

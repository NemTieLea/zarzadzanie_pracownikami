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


managerowie = []
pracownicy = []


while True:
    akcja = input('utworz / zarzadzaj / koniec: ')
    if akcja == 'koniec':
        print("Koncze")
        break
    elif akcja == 'utworz':
        while True:
            akcja_wewnetrzna = input('manager / pracownik / koniec')
            if akcja_wewnetrzna == 'koniec':
                break
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
            akcja_wewnetrzna = input('stanowisko / podwladni / bilans / koniec')
            if akcja_wewnetrzna == 'koniec':
                break
            elif akcja_wewnetrzna == 'stanowisko':
                nazwa_stanowiska = input('nazwa stanowiska: ')
                for p in pracownicy:
                    if p.stanowisko == nazwa_stanowiska:
                        print(p)
            elif akcja_wewnetrzna == 'podwladni':
                manager_name = input('imie nazwisko managera: ')
                # Dla kazdego managera
                for m in managerowie:
                    # sprawdz czy to ten, o ktory prosimy
                    if m.imie_nazwisko == manager_name:
                        print(m)
                        # dla kazdego pracownika
                        for p in pracownicy:
                            if p.nazwa_dzialu == m.nazwa_dzialu:
                                # jesli tak, to ypisz pracownika
                                print(p)
            else:
                print("nie ma takiej komendy")
    else:
        print("Nie ma takiej komendy...")

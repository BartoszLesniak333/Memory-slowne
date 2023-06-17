import re

#funkcja dodająca nick z wynikiem
def dodaj_wynik(nazwa, wynik):
    nick = input("Podaj swój nick, aby zapisać twój wynik: ")
    nazwa = nick

    with open('wyniki.txt', 'r') as file:
        lines = file.readlines()

    min_wynik = float('inf')
    min_wynik_index = None  # Indeks najmniejszej wartości

    for i, line in enumerate(lines):
        match = re.search(r'(\d+) pkt', line)
        if match:
            stary_wynik = int(match.group(1))

            if stary_wynik < min_wynik:
                min_wynik = stary_wynik
                min_wynik_index = i

    if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
        lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

        with open('wyniki.txt', 'w') as file:
            file.writelines(lines)
    else:
        print("Twój wynik nie jest większy od najmniejszego wyniku.")


# przykładowe wywołanie funkcji

nick = input("Podaj nick: ")
wynik = input("Podaj wynik: ")
dodaj_wynik(nick,wynik)

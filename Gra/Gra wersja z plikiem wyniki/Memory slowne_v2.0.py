import sys
import os
import time
import re
import threading

latwy = ('jabłko', 'gruszka', 'banan', 'pomarańcza', 'malina', 'brzoskwinia')  # probna lista
sredni = ('ojciec', 'wynik','arbuz', 'śliwka', 'cytryna', 'truskawka')  # probna lista
trudny = ('walic', 'nie wiem','Motyl','Deska','Słońce','Delfin','Arbuz','Balon')  # probna lista
sprawdzanie = []

#funkcjsa zpaisująca wyniki podczas gry

def dodaj_wynik(nick, wynik):

    with open('wyniki.txt', 'r') as file:
        lines = file.readlines()

    min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
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

def zwalnianie():
    sprawdzanie.clear()


def latwy_ilosc():
    n = len(latwy)
    print("Zapamiętaj słowa masz na to 5 min.")  # wywolywanie slow
    for i in range(0, n):
        print(latwy[i])
    time.sleep(1)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik = 0
    x = 0
    while x < n:
        slowo = str(input("Podaj słowo: \n"))
        m = len(sprawdzanie)
        for i in range(0, m):  # sprawdzanie czy slowo sie nie powtorzylo
            if slowo == sprawdzanie[i]:
                print("Powtorzone slowo")
                time.sleep(2)
                os.system("cls")
                kontyuowanie(wynik)

        if slowo in latwy:  # dodawanie punktow za dobre slowo
            wynik += 1
        else:  # konczenie programu
            print("Zle slowo")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(1)
        os.system("cls")
        x += 1
    kontyuowanie(wynik)


def sredni_ilosc():
    n = len(sredni)
    print(
        "Zapamiętaj słowa masz na to 5 min.")  # wywolywanie slow
    for i in range(0, n):
        print(sredni[i])
    time.sleep(1)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik = 0
    x = 0
    while x < n:
        slowo = str(input("Podaj słowo: \n"))
        m = len(sprawdzanie)
        for i in range(0, m):  # sprawdzanie czy slowo sie nie powtorzylo
            if slowo == sprawdzanie[i]:
                print("Powtorzone slowo")
                os.system("cls")
                kontyuowanie(wynik)

        if slowo in sredni:  # dodawanie punktow za dobre slowo
            wynik += 1
        else:  # konczenie programu
            print("Zle slowo")
            time.sleep(2)
            os.system("cls")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(1)
        os.system("cls")
        x += 1
    kontyuowanie(wynik)


def trudny_ilosc():
    n = len(trudny)
    print(
        "Zapamiętaj słowa masz na to 5 min.")  # wywolywanie slow
    for i in range(0, n):
        print(trudny[i])
    time.sleep(1)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik = 0
    x = 0
    while x < n:
        slowo = str(input("Podaj słowo: \n"))
        m = len(sprawdzanie)
        for i in range(0, m):  # sprawdzanie czy slowo sie nie powtorzylo
            if slowo == sprawdzanie[i]:
                print("Powtorzone slowo")
                kontyuowanie(wynik)

        if slowo in trudny:  # dodawanie punktow za dobre slowo
            wynik += 1
        else:  # konczenie programu
            print("Zle slowo")
            time.sleep(2)
            os.system("cls")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(1)
        os.system("cls")
        x += 1
    kontyuowanie(wynik)


def koniec():
    print("Dziekujemy za granie!")
    sys.exit(0)


def kontyuowanie(wynik):  # koncowa funkcja ma pokazywac wynik
    zwalnianie()
    print("Ostateczny wynik:", wynik, "pkt")

    nick = input("Podaj nick w celu zapisania twojego wyniku: ")
    dodaj_wynik(nick, wynik) # wywołanie funkcji która zapisze wynik oraz nick osoby do osobnego pliku

    koniec = str(input("Czy chcesz wyjsc z programu? y/n \n"))
    if koniec == 'y':
        sys.exit(0)
    if koniec == 'n':
        os.system("cls")
        main()


def ilosc():  # tryb do ilosci
    print("Wybór poziomu trudności. \n1.Latwy \n2.Sredni \n3.Trudny")
    wybor = int(input("Wybierz poziom trudnosci:"))
    if wybor == 1:
        os.system("cls")
        latwy_ilosc()
    if wybor == 2:
        os.system("cls")
        sredni_ilosc()
    if wybor == 3:
        os.system("cls")
        trudny_ilosc()


def latwy_czas():
    n = len(latwy)
    print("Zapamiętaj słowa masz na to 5 min.")  # wywolywanie slow
    for i in range(0, n):
        print(sredni[i])
    time.sleep(300)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik = 0
    t1 = time.time()
    x = 0
    while x < n:
        t2 = time.time()
        if t2 - t1 == 900 or t2 - t1 > 900:
            kontyuowanie(wynik)
        else:
            slowo = str(input("Podaj słowo: \n"))
            m = len(sprawdzanie)
            for i in range(0, m):  # sprawdzanie czy slowo sie nie powtorzylo
                if slowo == sprawdzanie[i]:
                    print("Powtorzone slowo")
                    time.sleep(2)
                    os.system("cls")
                    kontyuowanie(wynik)
            if slowo in latwy:  # dodawanie punktow za dobre slowo
                wynik += 1
                sprawdzanie.append(slowo)
                print("Dobre slowo")
                time.sleep(1)
                os.system("cls")
            else:  # konczenie programu
                print("Zle slowo")
                kontyuowanie(wynik)
        x += 1
    kontyuowanie(wynik)


def sredni_czas():
    n = len(sredni)
    print(
        "Zapamiętaj słowa masz na to 5 min.")  # wywolywanie slow
    for i in range(0, n):
        print(sredni[i])
    time.sleep(300)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik = 0
    t1 = time.time()
    x = 0
    while x < n:
        t2 = time.time()
        if t2 - t1 == 720 or t2 - t1 > 720:
            kontyuowanie(wynik)
        else:
            slowo = str(input("Podaj słowo: \n"))
            m = len(sprawdzanie)
            for i in range(0, m):  # sprawdzanie czy slowo sie nie powtorzylo
                if slowo == sprawdzanie[i]:
                    print("Powtorzone slowo")
                    time.sleep(2)
                    os.system("cls")
                    kontyuowanie(wynik)
            if slowo in sredni:  # dodawanie punktow za dobre slowo
                wynik += 1
                sprawdzanie.append(slowo)
                print("Dobre slowo")
                time.sleep(1)
                os.system("cls")
            else:  # konczenie programu
                print("Zle slowo")
                kontyuowanie(wynik)
        x += 1
    kontyuowanie(wynik)


def trudny_czas():
    n = len(trudny)
    print("Zapamiętaj słowa masz na to 5 min.")  # wywolywanie slow
    for i in range(0, n):
        print(sredni[i])
    time.sleep(300)
    os.system("cls")
    print("Powodzenia!! \nGra zacznie się za:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("cls")
    wynik = 0
    t1 = time.time()
    x = 0
    while x < n:
        t2 = time.time()
        if t2 - t1 == 600 or t2 - t1 > 600:
            kontyuowanie(wynik)
        else:
            slowo = str(input("Podaj słowo: \n"))
            m = len(sprawdzanie)
            for i in range(0, m):  # sprawdzanie czy slowo sie nie powtorzylo
                if slowo == sprawdzanie[i]:
                    print("Powtorzone slowo")
                    time.sleep(2)
                    os.system("cls")
                    kontyuowanie(wynik)
            if slowo in trudny:  # dodawanie punktow za dobre slowo
                wynik += 1
                sprawdzanie.append(slowo)
                print("Dobre slowo")
                time.sleep(1)
                os.system("cls")
            else:  # konczenie programu
                print("Zle slowo")
                kontyuowanie(wynik)
        x += 1
    kontyuowanie(wynik)


def na_czas():  # tryb gry na czas
    print("Wybór poziomu trudności. \n1.Latwy \n2.Sredni \n3.Trudny")
    wybor = int(input("Wybierz poziom trudnosci:"))
    if (wybor == 1):
        os.system("cls")
        latwy_czas()
    if (wybor == 2):
        os.system("cls")
        sredni_czas()
    if (wybor == 3):
        os.system("cls")
        trudny_czas()


def main():  # glowna funkcja
    print("Menu \n1. Ilosc\n2. Na czas\n3. Wyjscie")
    wybor = int(input("Wybierz tryb: "))  # zapytanie o wybor
    if (wybor == 1):
        os.system("cls")
        ilosc()
    if (wybor == 2):
        os.system("cls")
        na_czas()
    if (wybor == 3):
        koniec()


main()  # wywolanie funckji glownej